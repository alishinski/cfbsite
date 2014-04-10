from django.conf.urls import patterns, url

from cfbdata import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^teamlist/', views.teamlist, name='teamlist'),
    url(r'^(?P<conference_code>\d+)/$', views.conference, name='conference'),
#    url(r'^(?P<school_name>\d+)/$', views.team, name='team'),
    url(r'^(?P<conference_code>\d+)/(?P<team_num_code>\d+)/$', views.team, name='team'),    
)
