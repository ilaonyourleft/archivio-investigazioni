# Generated by Django 4.2.3 on 2023-07-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('tipo', models.CharField(max_length=100, verbose_name='tipo')),
            ],
        ),
    ]
