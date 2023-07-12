# Generated by Django 4.2.3 on 2023-07-10 18:40

from django.db import migrations


def create_data(apps, schema_editor):
    archivio = apps.get_model('archivio', 'Archivio')
    archivio(nome='VISITATORI', fkUtente=1).save()
    archivio(nome='PROVE', fkUtente=1).save()
    archivio(nome='BACCHETTE', fkUtente=1).save()
    archivio(nome='COLLABORATORI', fkUtente=1).save()


class Migration(migrations.Migration):

    dependencies = [
        ('archivio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
