from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checklist/', include('checklist.urls')),
    path('', RedirectView.as_view(url='/checklist/', permanent=False)),  # Redireciona para /checklist/
]
