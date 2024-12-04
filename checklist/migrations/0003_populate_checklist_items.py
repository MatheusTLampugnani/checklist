from django.db import migrations

def populate_checklist_items(apps, schema_editor):
    ChecklistItem = apps.get_model('checklist', 'ChecklistItem')
    items = [
        "Pisca dianteiro",
        "Lanterna Dianteira",
        "Regulagem de Farol",
        "Farol Baixo",
        "Farol Alto",
        "Farol de Neblina",
        "Farol de Milha",
        "Lanterna de Neblina",
        "Para-Choque Dianteiro",
        "Pisca Traseiro",
        "Lâmpada de Freio",
        "Lanterna Traseira",
        "Lâmpada de Ré",
        "Lâmpada da placa",
        "Para-Choques Traseiro",
        "Ponteira do Escape",
        "Engate",
        "Pintura",
        "Antena",
        "Chave / Fechaduras",
        "Controle Remoto / Travas / Conforto",
        "Estepe / chave de roda / triângulo / macaco",
        "Tapetes",
        "Extintor de incêndio",
        "Bancos",
        "Cinto de segurança",
        "Lampadas Internas e Cortesia",
        "Esguichador Pára-Brisa / Traseiro",
        "Palhetas / Limp. de Pára-Brisa",
        "Palhetas / Limp. Traseiro",
        "Buzina",
        "Ventilação Interna Quente e Frio",
        "Som / Alto Falantes",
        "Filtro de Cabine (Pólen)",
        "Higienização A/C",
        "Painel (ponteiros e iluminação)",
        "Altura e Pressão do Pedal de Embr.",
        "Altura e Pressão do Pedal de Freio",
        "Altura e Pressão do Pedal de Acel.",
        "Freio de estacionamento",
        "Freio de estacionamento elétrico",
        "Alavanca de Mudança de Marcha",
        "Retrovisores",
        "Retrovisores elétricos (programação?)",
        "Vidro elétrico (programação?)",
        "Insulfilm"
    ]
    for item in items:
        ChecklistItem.objects.get_or_create(description=item)

class Migration(migrations.Migration):
    dependencies = [
        ('checklist', '0002_populate_checklist_items'),  # Substitua 'xxxx_auto' pela última migração antes dessa
    ]

    operations = [
        migrations.RunPython(populate_checklist_items),
    ]
