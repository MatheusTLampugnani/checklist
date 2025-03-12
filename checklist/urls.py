from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ChecklistItemViewSet, ChecklistGroupViewSet, ChecklistDetailViewSet

router = DefaultRouter()
router.register(r'checklist-items', ChecklistItemViewSet, basename='checklist-item')
router.register(r'checklist-groups', ChecklistGroupViewSet, basename='checklist-group')
router.register(r'checklist-details', ChecklistDetailViewSet, basename='checklist-detail')

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('checklist/', views.checklist_view, name='checklist'),
    path('historico/', views.checklist_history, name='history'),
    path('historico/<int:group_id>/', views.history_detail, name='history_detail'),
    path('gerar-pdf/<int:group_id>/', views.generate_pdf, name='generate_pdf'),
    path('admin-checklist/', views.admin_checklist_view, name='admin_checklist'),


    # Rotas da API REST
    path('api/', include(router.urls)),
]
