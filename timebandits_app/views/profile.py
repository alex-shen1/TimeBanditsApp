"""Contains profile views"""
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from ..models import Account
from ..models import Task

class ProfileView(generic.DetailView):
    template_name = 'profile/profile.html'
    model = Account
    context_object_name = 'account'

    #def get_queryset(self):
        #pk = self.kwargs['pk']
    #    return Account.objects.all()
    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['tasks_owned'] = Task.objects.filter(owner=pk)
        context['tasks_registered'] = Task.objects.filter(registered_accounts=pk)
        return context

def profile(request):
    return HttpResponseRedirect("/profile/" + str(request.user.account.id))

def edit_profile(request, pk):
    """Edit profile page"""
    #Add check to only allow user to edit
    context = {'pk': pk}
    return render(request, 'profile/profile_edit.html', context)

def add_skill(request, pk):
    """Edit profile page"""
    #Add check to only allow user to edit
    context = {'pk': pk}
    return render(request, 'profile/profile_edit.html', context)