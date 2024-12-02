from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from checklist import views as checklist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', checklist_views.index, name='index'),  # Rota para a página inicial
    path('checklist/', include('checklist.urls')),
]
