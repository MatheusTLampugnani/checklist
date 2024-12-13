from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import ChecklistItem, ChecklistDetail, ChecklistGroup


def index(request):
    return render(request, 'index.html')


@login_required
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
            return redirect('history')

    return render(request, 'checklist.html', {'items': items})


@login_required
def checklist_history(request):
    groups = ChecklistGroup.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'groups': groups})


@login_required
def history_detail(request, group_id):
    group = get_object_or_404(ChecklistGroup, id=group_id, user=request.user)
    details = ChecklistDetail.objects.filter(group=group).select_related('item')
    return render(request, 'history_detail.html', {'group': group, 'details': details})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
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
        if request.GET.get('next'):
            messages.error(request, "Você precisa estar logado para acessar essa página.")
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')
