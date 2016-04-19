from django.db import models
from datetime import datetime


class Opportunity(models.Model):
    opportunity_id = models.AutoField(primary_key=True)
    opportunity_title = models.CharField(max_length=200)
    opportunity_details = models.CharField(max_length=200)
    opportunity_requirements = models.CharField(max_length=200, default = "None")
    hours_earned = models.PositiveIntegerField(default=1)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField('date')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        verbose_name_plural = "opportunities"

    def __str__(self):
        return self.opportunity_title


class Volunteer(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    volunteer_name = models.CharField(max_length=100)
    volunteer_email = models.EmailField(max_length=100)
    volunteer_grade = models.PositiveIntegerField(default=1)
    volunteer_detail = models.CharField(max_length=200, default = "N/A")

    def __str__(self):
        return self.volunteer_name
