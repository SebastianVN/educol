# Generated by Django 2.1 on 2018-10-13 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Educol', '0003_actividad_evento_usuarioevento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioevento',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Educol.Evento'),
        ),
    ]