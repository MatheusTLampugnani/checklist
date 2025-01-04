from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('checklist/', views.checklist_view, name='checklist'),
    path('historico/', views.checklist_history, name='history'),
    path('historico/<int:group_id>', views.history_detail, name='history_detail'),
    path('gerar-pdf/<int:group_id>/', views.generate_pdf, name='generate_pdf'),
]
