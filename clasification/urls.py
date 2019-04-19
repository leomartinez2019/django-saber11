from django.conf.urls import url
from . import views

app_name = 'clasification'
urlpatterns = [
    url(r'^$', views.index, name='clasificacion'),
    url(r'^(?P<dato_pk>[0-9]+)/$', views.detalle, name='detalle'),
]
