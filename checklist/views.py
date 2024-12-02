from django.shortcuts import render, redirect
from django.http import Http404
from .models import ChecklistItem, ChecklistSession

# Página inicial
def index(request):
    return render(request, 'index.html')

# Checklist existente
def checklist_view(request):
    items = ChecklistItem.objects.all()

    if request.method == 'POST':
        # Coleta os dados do formulário
        person_name = request.POST.get('person_name')
        car_plate = request.POST.get('car_plate')

        if person_name and car_plate:
            # Cria uma nova sessão de checklist
            session = ChecklistSession.objects.create(
                person_name=person_name,
                car_plate=car_plate
            )

            # Atualiza os itens com os status escolhidos
            for item in items:
                status = request.POST.get(f'status_{item.id}')
                if status:
                    item.status = status
                    item.save()

            return redirect('checklist')

    return render(request, 'checklist.html', {'items': items})
