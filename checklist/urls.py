from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='checklist_index'),  # Página inicial do checklist
    path('login/', views.user_login, name='login'),  # Página de login (caso personalizada)
    path('register/', views.register, name='register'),  # Página de registro
    path('checklist/', views.checklist_view, name='checklist'),
]
