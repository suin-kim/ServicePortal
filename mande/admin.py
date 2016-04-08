from django.contrib import admin
from .models import Opportunity, Volunteer

class VolunteerInline(admin.TabularInline):
    model = Volunteer
    extra = 0

class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('opportunity_title', 'date', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['opportunity_title']
    inlines = [VolunteerInline]

admin.site.register(Opportunity, OpportunityAdmin)
