# Generated by Django 3.2.10 on 2024-05-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basededados', '0009_auto_20240528_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_bio', models.ImageField(upload_to='portfolioapp/images/')),
                ('portuguese_bio', models.CharField(max_length=180)),
                ('knowledge_portuguese_title', models.CharField(max_length=180)),
                ('knowledge_english_title', models.CharField(max_length=180)),
                ('knowledge_portuguese_description', models.CharField(max_length=180)),
                ('knowledge_english_description', models.CharField(max_length=180)),
                ('project_portuguese_title', models.CharField(max_length=180)),
                ('project_english_title', models.CharField(max_length=180)),
                ('project_portuguese_description', models.CharField(max_length=180)),
                ('project_english_description', models.CharField(max_length=180)),
                ('experience_portuguese_title', models.CharField(max_length=180)),
                ('experience_english_title', models.CharField(max_length=180)),
                ('experience_portuguese_description', models.CharField(max_length=180)),
                ('experience_english_description', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Stacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='portfolioapp/images/')),
                ('stack_title', models.CharField(max_length=180)),
                ('stack_level', models.IntegerField()),
            ],
        ),
    ]
