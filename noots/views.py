from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import IntroDescreption, noots

# Create your views here.

NOOTS_TITLE :str
NOOTS_TEXT: str
NOOTS_LIST = []

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

def noots_page(request):
    
    template = loader.get_template('noots_page.html')
    return HttpResponse(template.render())

def write_noots(request):
    template = loader.get_template('noots-write.html')
    return HttpResponse(template.render()   )

def add_noots(request):
    NOOTS_TITLE = request.POST.get('title')
    NOOTS_TEXT = request.POST.get('text')
    NOOTS_LIST.append(noots(NOOTS_TITLE, NOOTS_TEXT))
    context = {
        'list': NOOTS_LIST
    }
    
    # template = loader.get_template('noots_page.html')
    return render(request, "noots_page.html", context)