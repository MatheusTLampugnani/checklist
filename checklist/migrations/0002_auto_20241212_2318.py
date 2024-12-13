from django.db import migrations

def populate_checklist_items(apps, schema_editor):
    ChecklistItem = apps.get_model('checklist', 'ChecklistItem')
    items = [
        "Óleo do Motor",
        "Fluido de Freio",
        "Líquido Arrefecimento do Motor",
        "Água do lavador do Para-Brisa",
        "Farol - Luz Baixa / Alta",
        "Iluminação - Lanternas / Freios / Ré",
        "Sinalização - Piscas",
        "Limpador Para-brisa",
        "Macaco e Cabo",
        "Chave de Roda",
        "Extintor",
        "Triângulo",
        "Pneu Estepe",
        "Riscos na Pintura",
        "Amassados",
        "Espelhos",
        "Para-brisa / Vidros",
        "Pneus - Desgaste / Calibragem",
        "Capota Marítima",
        "Outros",
        "Documento do Veículo / Cartão Abastecimento",
    ]
    for item in items:
        ChecklistItem.objects.get_or_create(description=item)

class Migration(migrations.Migration):
    dependencies = [
        ('checklist', '0001_initial'),  # Substitua 'xxxx_auto' pela última migração antes dessa
    ]

    operations = [
        migrations.RunPython(populate_checklist_items),
    ]