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

from . import views

app_name = "project"
urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html")),
    path('', views.TasksView.as_view()),
    path('profile', views.profile, name="profile"),
    path('profile/<int:pk>', views.ProfileView.as_view(), name="profileview"),
    path('profile/<int:pk>/edit', views.edit_profile),
    path(
        'profile/<int:pk>/edit/addskill',
        views.add_skill,
        name="addskill"),
    # Not implemented
    path('tasks', views.TasksView.as_view()),
    path('tasks/search', views.search, name='search'),
    path('tasks/create', views.create_task),
    path("tasks/charge", views.charge, name="charge"),
    path('tasks/<int:pk>/delete', views.delete_task, name='delete'),
    path('tasks/<int:pk>/edit', views.update_task, name='edit'),
    path('tasks/<int:pk>/join', views.join_task, name='join'),
    path('tasks/<int:pk>', views.TaskDetailsView.as_view(), name="details"),
    path('charities', views.CharitiesView.as_view()),
    path('about', views.about_view),
    path('leaderboard', views.LeaderboardView.as_view(), name='leaderboard')
]
