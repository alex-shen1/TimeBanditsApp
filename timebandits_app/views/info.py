"""Views related to miscellaneous site info."""
# pylint: disable=too-many-ancestors

from django.views import generic
from django.shortcuts import render
from ..models import Charity, Account


def about_view(request):
    """About page view."""
    return render(request, 'info/about.html')


class CharitiesView(generic.ListView):
    """Displays the list of charities."""
    template_name = 'info/charities.html'
    model = Charity


class LeaderboardView(generic.ListView):
    """View for leaderboard page"""
    template_name = 'info/leaderboard.html'
    context_object_name = 'leaderboard'

    def get_queryset(self):
        return Account.objects.all().order_by('total_hours')
