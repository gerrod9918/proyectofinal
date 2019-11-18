# Generated by Django 2.2.7 on 2019-11-18 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('seccion', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('credito', models.IntegerField()),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'profesor',
                'verbose_name_plural': 'profesores',
            },
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucucion.Grado')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucucion.Materia')),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucucion.Profesor'),
        ),
        migrations.AddField(
            model_name='grado',
            name='materias',
            field=models.ManyToManyField(related_name='get_materias', through='institucucion.Pensum', to='institucucion.Materia'),
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucucion.Grado')),
            ],
            options={
                'verbose_name': 'estudiante',
                'verbose_name_plural': 'estudiantes',
            },
        ),
    ]