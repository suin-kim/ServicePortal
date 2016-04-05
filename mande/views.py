from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Job, Volunteer
from .forms import VolunteerForm

def home(request):
    job = Job.objects.all()
    return render(request, 'mande/home.html', {'jlist': job})

def detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    form = VolunteerForm(request.POST or None)
    if form.is_valid():
        vol = form.save(commit=False)
        vol.job = job
        vol.save()
        return HttpResponseRedirect('results')
    return render(request, 'mande/detail.html', {'form':form, 'job' : job,'n' : range(1,13)})

def results(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'mande/results.html', {'job' : job})
