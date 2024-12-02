from django.urls import path
from . import views

urlpatterns = [
    path('', views.checklist_view, name='checklist'),
]
