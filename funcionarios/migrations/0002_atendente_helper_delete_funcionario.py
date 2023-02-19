# Generated by Django 4.1.6 on 2023-02-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
    ]
