# Generated by Django 4.1.7 on 2023-03-17 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alerta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concordo_text', models.CharField(max_length=20)),
                ('nãoconcordo_text', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolha', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='duvidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=8)),
                ('pergunta', models.CharField(max_length=200)),
                ('resposta', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='paginainicial',
            fields=[
                ('home_text', models.BigAutoField(primary_key=True, serialize=False)),
                ('publicacao_date', models.DateTimeField(verbose_name=' date published ')),
            ],
        ),
        migrations.CreateModel(
            name='servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('senha', models.CharField(max_length=8)),
                ('escolha_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cadastro')),
            ],
        ),
        migrations.AddField(
            model_name='cadastro',
            name='home_text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.paginainicial'),
        ),
        migrations.CreateModel(
            name='aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('senha', models.CharField(max_length=8)),
                ('matricula', models.IntegerField(max_length=10)),
                ('escolha_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cadastro')),
            ],
        ),
    ]
