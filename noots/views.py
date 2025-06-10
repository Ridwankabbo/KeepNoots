from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import IntroDescreption

# Create your views here.

def home(request):
    introDec = IntroDescreption(
        "Organize Your Thoughts, Unleash Your Potential.",
        "Noots App helps you capture ideas, create notes, and stay productive with ease." ,
        "Ready to Get Organized With Mobile Applications?"
        )
    # introDec.intro = "Organize Your Thoughts, Unleash Your Potential."
    # introDec.slogan ="Noots App helps you capture ideas, create notes, and stay productive with ease." 
    # introDec.title_for_mobile_app = "Ready to Get Organized With Mobile Applications?"
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'intro_decs': introDec}))
    #return render(request, "index.html", {'intro_decs': introDec})

def singUp(request):
    template = loader.get_template('singup.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())