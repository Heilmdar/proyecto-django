# Generated by Django 3.2.4 on 2021-07-07 18:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='coment',
            field=ckeditor.fields.RichTextField(verbose_name='Comentario'),
        ),
    ]
