from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .models import ChecklistItem, ChecklistDetail, ChecklistGroup
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
from datetime import datetime


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def checklist_view(request):
    items = ChecklistItem.objects.all()
    if request.method == 'POST':
        car_plate = request.POST.get('car_plate')
        if car_plate:
            checklist_group = ChecklistGroup.objects.create(
                car_plate=car_plate,
                user=request.user
            )
            for item in items:
                status = request.POST.get(f'status_{item.id}')
                if status:
                    ChecklistDetail.objects.create(
                        user=request.user,
                        item=item,
                        car_plate=car_plate,
                        status=status,
                        group=checklist_group
                    )
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para acessar sua conta.')
            return redirect('index')
    return render(request, 'checklist.html', {'items': items})


@login_required(login_url='/login/')
def checklist_history(request):
    groups = ChecklistGroup.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'groups': groups})


@login_required(login_url='/login/')
def history_detail(request, group_id):
    group = get_object_or_404(ChecklistGroup, id=group_id, user=request.user)
    details = ChecklistDetail.objects.filter(group=group).select_related('item')
    return render(request, 'history_detail.html', {'group': group, 'details': details})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao realizar o cadastro.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return redirect('index')


@login_required(login_url='/login/')
def generate_pdf(request, group_id):
    group = get_object_or_404(ChecklistGroup, id=group_id, user=request.user)
    
    details = ChecklistDetail.objects.filter(group=group).select_related('item')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="checklist_{group.car_plate}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    header = Paragraph(f'<strong>Relatório do Checklist: {group.car_plate}</strong>', styles['Title'])
    elements.append(header)

    data = [['Item', 'Status', 'Data']]
    for detail in details:
        data.append([
            detail.item.description,
            detail.get_status_display(),
            detail.created_at.strftime('%d/%m/%Y %H:%M')
        ])

    table = Table(data)
    table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ]))

    elements.append(table)

    footer = Paragraph(f'Gerado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}', styles['Normal'])
    elements.append(footer)

    doc.build(elements)

    return response

