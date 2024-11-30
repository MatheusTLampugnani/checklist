from django.shortcuts import render, redirect
from django.http import Http404
from .models import ChecklistItem
from .forms import ChecklistItemForm

def checklist_view(request):
    items = ChecklistItem.objects.all()

    if request.method == 'POST':
        # Para cada item no formulário, obtém o valor do status e o ID do item
        for item in items:
            item_id = request.POST.get(f'item_id_{item.id}')
            status = request.POST.get(f'status_{item.id}')
            
            # Verifica se o item_id e o status são válidos
            if item_id and status:
                try:
                    checklist_item = ChecklistItem.objects.get(id=item_id)
                    checklist_item.status = status  # Atualiza o status do item
                    checklist_item.save()  # Salva a mudança no banco de dados
                except ChecklistItem.DoesNotExist:
                    raise Http404("Item não encontrado")

        return redirect('checklist')  # Redireciona de volta para a página de checklist

    return render(request, 'checklist.html', {'items': items})
