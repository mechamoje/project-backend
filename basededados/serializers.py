from rest_framework import serializers
from .models import AboutMe, Project, Stacks


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['cover', 'title', 'demo', 'github', 'type']


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ['english_bio', 'portuguese_bio', 'knowledge_portuguese_title', 'knowledge_english_title',
                  'knowledge_portuguese_description', 'knowledge_english_description', 'project_portuguese_title', 'project_english_title', 'portuguese_bio',
                  'project_portuguese_description', 'project_english_description', 'experience_portuguese_title', 'experience_english_title',
                  'experience_portuguese_description', 'experience_english_description']


class StacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stacks
        fields = ['icon', 'stack_title', 'stack_level']
