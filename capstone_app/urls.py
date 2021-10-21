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
    path('add-current', views.add_current, name='add_current'),
    path('add-read', views.add_read, name='add_read'),
    path('add-want', views.add_want, name='add_want'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

