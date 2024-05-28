# Generated by Django 3.2.10 on 2024-05-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basededados', '0010_aboutme_stacks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='english_bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='experience_english_description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='experience_english_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='experience_portuguese_description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='experience_portuguese_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='knowledge_english_description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='knowledge_english_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='knowledge_portuguese_description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='knowledge_portuguese_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='portuguese_bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='project_english_description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='project_english_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='project_portuguese_description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='project_portuguese_title',
            field=models.CharField(max_length=50),
        ),
    ]
