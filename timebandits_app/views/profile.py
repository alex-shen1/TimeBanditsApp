"""Contains profile views"""
from django.shortcuts import render


def profile(request):
    """Profile view"""
    return render(request, 'profile/profile.html', {'test': "THIS WORKS"
                                                    })


def edit_profile(request):
    """Edit profile page"""
    return render(request, 'profile/profile_edit.html')
