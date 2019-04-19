from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^mychart$', TemplateView.as_view(template_name="mychart.html")),
    url(r'^google7ecc988dde80334f.html$', TemplateView.as_view(template_name="google-search.html")),
    url(r'^saber2017/', include('saber2017.urls')),
    url(r'^saber2016/', include('saber2016.urls')),
    url(r'^clasificacion/', include('clasification.urls')),
]
