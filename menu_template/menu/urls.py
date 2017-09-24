from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<url>[^ \f\n\r\t\v]+)$', views.main, name='main'),
    url(r'^(?P<url>)$', views.main, name='main')
]