from django.forms import ModelForm
from .models import Volunteer

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        exclude = ['opportunity']

    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        #for field in iter(self.fields):
        self.fields['volunteer_name'].widget.attrs.update({
            'id': 'name',
            'class': 'form-control'
        })
        self.fields['volunteer_email'].widget.attrs.update({
            'id': 'email',
            'class': 'form-control'
        })
        self.fields['volunteer_grade'].widget.attrs.update({
            'id': 'grade',
            'class': 'form-control'
        })
        self.fields['volunteer_detail'].widget.attrs.update({
            'id': 'detail',
            'class': 'form-control'
        })
