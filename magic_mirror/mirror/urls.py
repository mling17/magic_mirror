"""magic_mirror URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'index/$', views.index, name='index'),
    re_path(r'^$', views.index),
    re_path(r'lunar/$', views.get_lunar, name='lunar'),
    re_path(r'interactive/$', views.interactive, name='interactive'),
    re_path(r'weather/$', views.weather, name='weather'),
    re_path(r'forecast/$', views.forecast, name='forecast'),
    re_path(r'temp_hum/$', views.temp_hum, name='temp_hum'),
    re_path(r'todo/$', views.todo, name='todo'),
    re_path(r'pi_info/$', views.pi_info, name='pi_info'),

]
