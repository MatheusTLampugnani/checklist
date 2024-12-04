from django.db import models

STATUS_CHOICES = [
    ('bom', 'Bom'),
    ('regular', 'Regular'),
    ('ruim', 'Ruim'),
]

class ChecklistItem(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, blank=True)  # Changed null=True to blank=True

    def __str__(self):
        return f"{self.description} - {self.status}"  # String representation of the model

class ChecklistSession(models.Model):
    person_name = models.CharField(max_length=100, verbose_name="Nome da Pessoa")
    car_plate = models.CharField(max_length=10, verbose_name="Placa do Carro")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Checklist for {self.person_name} - {self.car_plate} ({self.created_at})"  # String representation of the model
