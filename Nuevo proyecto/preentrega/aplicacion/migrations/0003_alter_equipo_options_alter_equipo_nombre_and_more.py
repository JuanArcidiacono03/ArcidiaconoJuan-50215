# Generated by Django 5.0.2 on 2024-03-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_alter_equipo_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipo',
            options={},
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='nombre',
            field=models.IntegerField(),
        ),
    ]
