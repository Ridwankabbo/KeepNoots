from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import IntroDescreption, noots
from noots.models import noots, Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


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

# def singUp(request):
#     template = loader.get_template('singup.html')
#     return HttpResponse(template.render())

def register_user(request):
    
    # .................. OLD methods .....................
    
    #user = Users()
    
    # if request.method == "GET":
    #     user_name = request.GET.get('username')
    #     email = request.GET.get('email')
    #     password = request.GET.get('password')
    #     c_password = request.GET.get('confirm_password')
        
    #     if password == c_password:
    #         user.name = user_name
    #         user.email = email
    #         user.password = password
    #         user.save()
            
    #         return redirect('noots-page')
    #     else:
    #         return redirect('singup')
    
    # ........................ NEW methods .....................
    
    if request.method == "GET":
        form = UserCreationForm(request.GET)
        if form.is_valid():
            login(request, form.save())
            return redirect('noots-page')
    else:
        form = UserCreationForm()
    
    return render(request, "singup.html", {"form": form})
    
    
        

def login(request):
    # template = loader.get_template('login.html')
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login(request, form.get_user())
            return redirect('noots-page')
    else:
        form = AuthenticationForm()    
    
    return render(request, "login.html", {'form': form})

def noots_page(request):
    
    # template = loader.get_template('noots_page.html')
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