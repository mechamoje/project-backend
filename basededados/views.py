from django.shortcuts import render
from .models import AboutMe, Project, Stacks
from .serializers import AboutMeSerializer, ProjectSerializer, StacksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def show_projects(request):
    projects = Project.objects.all()
    serialized = ProjectSerializer(projects, many=True)
    return Response(serialized.data)


@api_view(['GET'])
def get_about_me_infos(request):
    about_me = AboutMe.objects.all()
    serialized = AboutMeSerializer()
    return Response(serialized.data)


@api_view(['GET'])
def get_stacks_infos(request):
    projects = Stacks.objects.all()
    serialized = StacksSerializer(many=True)
    return Response(serialized.data)
