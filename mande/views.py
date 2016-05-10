from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Opportunity, Volunteer
from .forms import VolunteerForm
from django.core.mail import send_mail

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
        send_mail('test email', 'hello world', 'suinkm4@email.com', ['sikim@student.logoscambodia.org'])
        vol.save()
        #return HttpResponseRedirect('results')
    return HttpResponseRedirect(reverse('mande:results', args=(opp_id)))

def results(request, opp_id):
    opportunity = get_object_or_404(Opportunity, pk=opp_id)
    return render(request, 'mande/results.html', {'opp' : opportunity})
