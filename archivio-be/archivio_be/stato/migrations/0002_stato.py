# Generated by Django 4.2.3 on 2023-07-10 18:40

from django.db import migrations


def create_data(apps, schema_editor):
    stato = apps.get_model('stato', 'Stato')
    stato(nome='APERTO', tipo='CASO').save()
    stato(nome='CHIUSO', tipo='CASO').save()
    stato(nome='CONGELATO', tipo='CASO').save()
    stato(nome='ARCHIVIATO', tipo='CASO').save()
    stato(nome='PUBBLICO', tipo='FASCICOLO').save()
    stato(nome='RISERVATO', tipo='FASCICOLO').save()


class Migration(migrations.Migration):

    dependencies = [
        ('stato', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
