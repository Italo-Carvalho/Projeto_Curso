# Generated by Django 3.1.5 on 2021-01-19 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20210119_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='media_avaliacoes',
        ),
    ]