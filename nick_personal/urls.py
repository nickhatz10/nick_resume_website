# this is important

"""nick_personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

# from local directory import views, this allows us to get the things from views.py
from . import views

# this basically defines the different extensions of the main url generated when the server is run
# example: www.cars.com (root url), www.cars/new_cars.com (url extension which would be defined below)
urlpatterns = [
    # empty string which means it's the root url
    # takes the output from the index function from the views.py file and puts it on the root url
    #path("", views.index, name="index"),
    path("", include("nick_personal.apps.public.urls")),
]
