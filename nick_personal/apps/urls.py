# important
from django.urls import path
from django.views.generic.base import TemplateView

# from local directory import views, this allows us to get the things from views.py
from nick_personal.apps import views

app_name = "public"
# this basically defines the different extensions of the main url generated when the server is run
# example: www.cars.com (root url), www.cars/new_cars.com (url extension which would be defined below)
urlpatterns = [
    # empty string which means it's the root url
    # takes the output from the index function from the views.py file and puts it on the root url
    path("", views.index, name="index"),
    #path("", views.index, name="index"),
    # makes a url extension for the about sub-page
    #path("about", views.about, name="about"),
    # makes a url extension for the contact sub-page
    #path("contact", views.contact, name="contact"),
    # points to our homepage in index.html as the path for the index root (what we first see when we go to the website)
    #path('', TemplateView.as_view(template_name = "index.html"), name = "index"),
]