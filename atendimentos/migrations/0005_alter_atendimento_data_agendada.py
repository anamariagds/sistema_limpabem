# Generated by Django 4.1.6 on 2023-02-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0004_alter_atendimento_data_agendada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='data_agendada',
            field=models.DateTimeField(),
        ),
    ]
