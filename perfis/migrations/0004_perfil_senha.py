# Generated by Django 2.2.2 on 2019-06-30 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_perfil_contatos'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='senha',
            field=models.CharField(default='aa', max_length=100),
            preserve_default=False,
        ),
    ]
