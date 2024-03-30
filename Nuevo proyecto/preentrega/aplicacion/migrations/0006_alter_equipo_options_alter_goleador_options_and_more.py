# Generated by Django 5.0.2 on 2024-03-27 02:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_alter_posicion_nombre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipo',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='goleador',
            options={'verbose_name': 'Goleador', 'verbose_name_plural': 'Goleadores'},
        ),
        migrations.AlterModelOptions(
            name='posicion',
            options={'verbose_name': 'Posicion', 'verbose_name_plural': 'Posiciones'},
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
