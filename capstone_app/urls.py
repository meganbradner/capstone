from django.urls import path 
from . import views

from django.conf import settings
from django.conf.urls.static import static 

app_name = 'capstone_app'

urlpatterns = [

    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('browse', views.browse, name='browse'),
    path('timeline', views.timeline, name='timeline'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

