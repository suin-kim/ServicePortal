from django.conf.urls import url
from . import views

app_name = 'mande'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<opp_id>[\d]+)/signup$', views.signup, name='signup'),
    url(r'^(?P<opportunity_id>[0-9]+)/results/$', views.results, name='results'),
]
