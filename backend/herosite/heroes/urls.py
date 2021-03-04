from django.conf.urls import url
from heroes import views
from django.urls import path


urlpatterns = [
    path('heroes', views.getHeroes),
    path('heroes/<int:pk>', views.getHero),
]