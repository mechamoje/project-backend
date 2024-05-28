from django.urls import path
from .views import get_about_me_infos, get_stacks_infos, show_projects

urlpatterns = [
    path('projects/', show_projects),
    path('aboutme/', get_about_me_infos),
    path('stacks/', get_stacks_infos),
]
