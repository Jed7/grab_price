from django.conf.urls import url
from app_grab import views

urlpatterns = [
    url(r'^$' , views.index, name='index'),
]
