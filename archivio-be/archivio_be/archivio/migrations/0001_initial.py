# Generated by Django 4.2.3 on 2023-07-10 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('fkUtente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utente.utente')),
            ],
        ),
    ]
