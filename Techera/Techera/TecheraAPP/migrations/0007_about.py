# Generated by Django 4.2.2 on 2023-07-02 22:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TecheraAPP', '0006_rename_mensajes_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='aboutImagenes')),
                ('mensaje', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]
