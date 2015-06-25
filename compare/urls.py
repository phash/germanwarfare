from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<fahrzeug_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<fahrzeug_id1>[0-9]+)/(?P<fahrzeug_id2>[0-9]+)/(?P<waffe_id1>[0-9]+)/(?P<waffe_id2>[0-9]+)/vergleich/$', views.vergleich, name='vergleich'),
]