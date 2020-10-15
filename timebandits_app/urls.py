"""timebandits_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('profile', views.profile),
    path('profile/edit', views.edit_profile),
    path('tasks', views.TasksView.as_view()),
    path('tasks/create', views.CreateTasksView.as_view()),
    path('tasks/<int:pk>', views.TaskDetailsView.as_view()),
    path('charities', views.CharitiesView.as_view()),
    path('about', views.about_view),
    path('leaderboard', views.leaderboard_view)
]
