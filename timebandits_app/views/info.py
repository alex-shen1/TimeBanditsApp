"""Views related to miscellaneous site info."""
# pylint: disable=too-many-ancestors

from django.views import generic
from django.shortcuts import render
from ..models import Charity


def about_view(request):
    """About page view."""
    return render(request, 'info/about.html')


class CharitiesView(generic.ListView):
    """Displays the list of charities."""
    template_name = 'info/charities.html'
    model = Charity


def leaderboard_view(request):
    """Displays public leaderboard."""
    return render(request, 'info/leaderboard.html')
