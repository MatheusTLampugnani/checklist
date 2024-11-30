from django.db import models

class ChecklistItem(models.Model):
    STATUS_CHOICES = [
        ('bom', 'Bom'),
        ('ruim', 'Ruim'),
        ('regular', 'Regular'),
    ]
    
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return self.description
