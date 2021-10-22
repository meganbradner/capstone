from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static 

app_name = 'users'

urlpatterns = [
    
    path('log_out/', views.log_out, name="log_out"),
    path('log_in/', views.log_in, name="log_in"),
    path('new_user/', views.new_user, name="new_user")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
