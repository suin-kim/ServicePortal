from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mande'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<opp_id>[\d]+)/signup$', views.signup, name='signup'),
    url(r'^(?P<opp_id>[0-9]+)/results/$', views.results, name='results'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
