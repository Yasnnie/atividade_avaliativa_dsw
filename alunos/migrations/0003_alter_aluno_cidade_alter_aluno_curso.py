# Generated by Django 4.2.6 on 2023-10-26 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
        ('cidades', '0001_initial'),
        ('alunos', '0002_aluno_cidade_aluno_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cidade',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cidades.cidade'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cursos.curso'),
        ),
    ]
