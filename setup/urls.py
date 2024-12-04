from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel administrativo
    path('', include('checklist.urls'))
]
