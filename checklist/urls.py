from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial do checklist
    path('login/', views.user_login, name='login'),  # Página de login (caso personalizada)
    path('register/', views.register, name='register'),  # Página de registro
    path('logout/', views.logout, name='logout'),
    path('checklist/', views.checklist_view, name='checklist'),
    path('historico/', views.checklist_history, name='history'),
    path('historico/<int:group_id>', views.history_detail, name='history_detail'),
    path('gerar-pdf/<int:group_id>/', views.generate_pdf, name='generate_pdf'),
]
