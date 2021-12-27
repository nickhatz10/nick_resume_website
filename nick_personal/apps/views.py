# important
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

'''
def index(request):
    return render(request, "index.html")
    template = loader.get_template("index.html")
    # will be able to pass in data for the index page
    return HttpResponse(template.render({}, request))


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
'''