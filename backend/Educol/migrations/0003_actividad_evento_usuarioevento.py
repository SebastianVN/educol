# Generated by Django 2.1 on 2018-10-13 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Educol', '0002_auto_20181008_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asistencia', models.IntegerField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Educol.Actividad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Educol.Usuario')),
            ],
        ),
    ]
