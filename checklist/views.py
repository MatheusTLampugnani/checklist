from django.shortcuts import render, redirect
from .models import ChecklistItem, ChecklistSession
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'index.html')  # Não há subpastas


def checklist_view(request):
    items = ChecklistItem.objects.all()

    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        car_plate = request.POST.get('car_plate')

        if person_name and car_plate:
            session = ChecklistSession.objects.create(
                person_name=person_name,
                car_plate=car_plate
            )

            for item in items:
                status = request.POST.get(f'status_{item.id}')
                if status:
                    item.status = status
                    item.save()

            return redirect('checklist')

    return render(request, 'checklist.html', {'items': items})  # Diretamente no templates/


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})  # Diretamente no templates/


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})  # Diretamente no templates/
