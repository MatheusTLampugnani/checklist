from django.db import models

STATUS_CHOICES = [
    ('bom', 'Bom'),
    ('regular', 'Regular'),
    ('ruim', 'Ruim'),
]

class ChecklistItem(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, null=True, blank=True)

class ChecklistSession(models.Model):
    person_name = models.CharField(max_length=100, verbose_name="Nome da Pessoa")
    car_plate = models.CharField(max_length=10, verbose_name="Placa do Carro")
    created_at = models.DateTimeField(auto_now_add=True)
