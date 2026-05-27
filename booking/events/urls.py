from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    re_path(r'^event/(?P<event_id>\d+)/$', views.event_detail, name='event_detail'),
]