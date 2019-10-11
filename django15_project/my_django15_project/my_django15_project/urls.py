from django.conf.urls import patterns, include, url
from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url('', views.home, name='home')
]
