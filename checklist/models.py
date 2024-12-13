from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário do Django


STATUS_CHOICES = [
    ('bom', 'Bom'),
    ('regular', 'Regular'),
    ('ruim', 'Ruim'),
]


class ChecklistItem(models.Model):
    description = models.CharField(
        max_length=255, 
        verbose_name="Descrição do Item"
    )  

    def __str__(self):
        return self.description

class ChecklistGroup(models.Model):
    car_plate = models.CharField(
        max_length=10, 
        verbose_name="Placa do Carro"
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='checklist_groups', 
        verbose_name='Usuário'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Data de Criação"
    )

    def __str__(self):
        return f"Grupo: {self.car_plate} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"

class ChecklistDetail(models.Model):
    car_plate = models.CharField(
        max_length=10, 
        verbose_name="Placa do Carro"
    )
    item = models.ForeignKey(
        ChecklistItem, 
        on_delete=models.CASCADE, 
        related_name="details", 
        verbose_name="Item do Checklist"
    )
    status = models.CharField(
        max_length=7, 
        choices=STATUS_CHOICES, 
        blank=True, 
        verbose_name="Status do Item"
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='checklist_details', 
        verbose_name='Usuário',
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    group = models.ForeignKey(
        ChecklistGroup, 
        on_delete=models.CASCADE, 
        related_name="group", 
        verbose_name="Grupo do Checklist"
    )

    def __str__(self):
        return f"{self.item.description} - {self.status} ({self.car_plate})"
