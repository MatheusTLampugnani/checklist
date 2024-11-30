from django import forms
from .models import ChecklistItem

class ChecklistItemForm(forms.ModelForm):
    class Meta:
        model = ChecklistItem
        fields = ['description', 'status']
        widgets = {
            'status': forms.Select(choices=ChecklistItem.STATUS_CHOICES),
        }
