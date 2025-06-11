from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import IntroDescreption, noots
from noots.models import noots


# Create your views here.

NOOTS_TITLE :str
NOOTS_TEXT: str
#NOOTS_LIST = []
NOOTS = noots()

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
    
    #template = loader.get_template('noots_page.html')
    # return HttpResponse(template.render())
    context = {
        'noots': noots.objects.all()
    }
    
    return render(request, "noots_page.html", context)

def write_noots(request):
    template = loader.get_template('noots-write.html')
    return HttpResponse(template.render())



def add_noots(request):
    # ..............OLD METHODS........................
    # NOOTS_TITLE = request.GET.get('title')
    # NOOTS_TEXT = request.GET.get('text')
    # NOOTS_LIST.append(noots(NOOTS_TITLE, NOOTS_TEXT))
    # context = {
    #     'list': NOOTS_LIST
    # }
    
    # template = loader.get_template('noots_page.html')
    # return render(request, "noots_page.html", context)
    
    
    #..................UPDATED METHODS......................
    
    if request.method == 'GET':
        NOOTS_TITLE = request.GET.get('title')
        NOOTS_TEXT = request.GET.get('text')
        
        NOOTS.title = NOOTS_TITLE
        NOOTS.text = NOOTS_TEXT
        NOOTS.save()
        
        
        # NOOTS.objects.create(
        #     title = NOOTS_TITLE,
        #     text = NOOTS_TEXT
        # )
    
    return redirect('noots-page')