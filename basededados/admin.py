from django.contrib import admin
from .models import AboutMe, Project, Stacks

# Register your models here.
admin.site.register(Project)
admin.site.register(AboutMe)
admin.site.register(Stacks)
