# Generated by Django 5.0.2 on 2024-03-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]
