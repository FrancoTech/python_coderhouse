# Generated by Django 4.2 on 2023-07-03 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TecheraAPP', '0009_alter_blogpost_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='descripcion',
        ),
    ]
