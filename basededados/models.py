from django.db import models

# Create your models here.


class Project(models.Model):
    cover = models.ImageField(upload_to='portfolioapp/images/')
    title = models.CharField(max_length=180)
    demo = models.URLField(blank=True)
    github = models.URLField(blank=True)
    type = models.CharField(
        max_length=50, choices=[('game', 'game'), ('project', 'project')], default='project')

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    english_bio = models.TextField()
    portuguese_bio = models.TextField()
    knowledge_portuguese_title = models.CharField(max_length=50)
    knowledge_english_title = models.CharField(max_length=50)
    knowledge_portuguese_description = models.CharField(max_length=50)
    knowledge_english_description = models.CharField(max_length=50)
    project_portuguese_title = models.CharField(max_length=50)
    project_english_title = models.CharField(max_length=50)
    project_portuguese_description = models.CharField(max_length=50)
    project_english_description = models.CharField(max_length=50)
    experience_portuguese_title = models.CharField(max_length=50)
    experience_english_title = models.CharField(max_length=50)
    experience_portuguese_description = models.CharField(max_length=50)
    experience_english_description = models.CharField(max_length=50)

    def __str__(self):
        return 'About me'


class Stacks(models.Model):
    icon = models.ImageField(upload_to='portfolioapp/images/')
    stack_title = models.CharField(max_length=180)
    stack_level = models.IntegerField()

    def __str__(self):
        return self.stack_title
