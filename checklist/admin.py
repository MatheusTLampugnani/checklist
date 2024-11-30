from django.contrib import admin
from .models import ChecklistItem

class ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'status')
    list_filter = ('status',)
    search_fields = ('description',)

admin.site.register(ChecklistItem, ChecklistItemAdmin)
