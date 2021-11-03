from django.urls import path 
from . import views

from django.conf import settings
from django.conf.urls.static import static 

app_name = 'capstone_app'

urlpatterns = [

    path('', views.index, name='index'),
    path('<slug:slug>', views.profile, name='profile'),
    path('browse', views.browse, name='browse'),
    path('timeline', views.timeline, name='timeline'),
    path('add-current', views.add_current, name='add_current'),
    path('add-read', views.add_read, name='add_read'),
    path('add-want', views.add_want, name='add_want'),
    path('finished/<int:id>', views.finished, name='finished'),
    path('like-update/<int:id>', views.like_update, name='like_update'),
    path('start-reading/<int:id>', views.start_reading, name='start_reading'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

