# Generated by Django 4.2.1 on 2023-10-25 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basededados', '0007_alter_distributor_options_alter_salesperson_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='activity',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Atividade'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='service',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Serviço'),
        ),
    ]