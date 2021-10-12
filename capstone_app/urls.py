from django.urls import path 
from . import views

app_name = 'capstone_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('browse', views.browse, name='browse'),
    path('timeline', views.timeline, name='timeline'),

]
