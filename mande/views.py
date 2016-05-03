from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Opportunity, Volunteer
from .forms import VolunteerForm

def home(request):
    opportunity = Opportunity.objects.all()
    form = VolunteerForm(request.POST or None)
    return render(request, 'mande/home.html', {'opplist': opportunity, 'form':form})

def signup(request, opp_id):
    opportunity = Opportunity.objects.all()
    select_opportunity = Opportunity.objects.get(pk=opp_id)
    form = VolunteerForm(request.POST or None)
    if form.is_valid():
        vol = form.save(commit=False)
        vol.opportunity = select_opportunity
        vol.save()
        #return HttpResponseRedirect('results')
    success = "You have successfully signed up!"
    return render(request, 'mande/home.html', {'success': success, 'opplist': opportunity, 'form':form})

def results(request, opportunity_id):
    opportunity = get_object_or_404(Opportunity, pk=opportunity_id)
    return render(request, 'mande/results.html', {'opp' : opportunity})
