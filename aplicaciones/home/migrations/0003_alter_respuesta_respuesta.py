# Generated by Django 3.2.6 on 2021-08-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_preguntas_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='respuesta',
            field=models.CharField(max_length=200),
        ),
    ]
