from django.conf.urls import url
from . import views

app_name = 'saber2016'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<slug>[\w+-]+)/(?P<pk>\d+)/detalle/$', views.detalle, name="detalle"),
    url(r'^listado/$', views.proc_colegio, name="proc_colegio"),
]
