# Generated by Django 4.2.1 on 2023-10-25 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basededados', '0006_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distributor',
            options={'ordering': ['company_name'], 'verbose_name': 'Distribuidor', 'verbose_name_plural': 'Distribuidores'},
        ),
        migrations.AlterModelOptions(
            name='salesperson',
            options={'ordering': ['name'], 'verbose_name': 'Vendedor', 'verbose_name_plural': 'Vendedores'},
        ),
    ]