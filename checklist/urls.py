from django.urls import path
from .views import checklist_view

urlpatterns = [
    path('', checklist_view, name='checklist'),
]
