from django.conf.urls import url
from heroes import views


urlpatterns = [
    url(r'^heroes$', views.getHeroes),
    url(r'^heroes/(?P<pk>[0-9]+)$', views.getHero),
]