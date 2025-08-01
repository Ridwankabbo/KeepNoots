from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import IntroDescreption, noots
from noots.models import noots
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse


# Create your views here.

NOOTS_TITLE :str
NOOTS_TEXT: str
#NOOTS_LIST = []
NOOTS = noots()

LOGED_USER_ID = 0

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

def register_user(request):
    
    """
    ..................................... DEFAULT REGISTRATION AUTH METHOD.........................
    
    if request.method == "GET":
        form = UserCreationForm(request.GET)
        if form.is_valid():
            login(request, form.save())
            return redirect('noots-page')
    else:
        form = UserCreationForm()
    
    return render(request, "singup.html", {"form": form})
    
    ................................................................................................
    
    """
    
    """.................................. CUSTOMIZE REGISTRATION AUTH METHOD............................."""
    
    
    
    if request.method == "GET":
        user_name = request.GET.get('username')
        email = request.GET.get('email')
        password = request.GET.get('password')
        c_password = request.GET.get('confirm_password')
        
        if password == c_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, "A user with this username already exists.")
                return redirect('singup')
            else:
                user = User.objects.create_user(username=user_name, email=email, password=password)
                user.save()
                messages.success(request, "Your account has created successfully")
            # user.name = user_name
            # user.email = email
            # user.password = password
            # user.save()
            
                auth_login(request, user)
                
                print(request.user.id)
            
                return redirect('noots-page')
        else:
            return redirect('singup')
        
    #return render(request, 'register-usr')
    
    
    
    
    
        

def login(request):
    # template = loader.get_template('login.html')
    
    """ ................................. DEFAULT LOGIN AUTH METHOD.........................................
    
    if request.method == "POST":
        form = AuthenticationForm(request= request, data=request.POST)
        if form.is_valid(): 
            user = form.get_user()
            print(user)
            auth_login(request, user)
           
            # # login(request, form.get_user())
            # user_name = form.cleaned_data.get('username')
            # LOGED_USER_ID = noots().objects.get()
            #LOGED_USER_ID = request.user.id
           
            return redirect('noots-page')
    else:
        form = AuthenticationForm()    
        
    
    return render(request, "login.html", {'form': form})
    
    """
    
    """.................................... cUSTOMIZE LOGIN AUTH MEHTOD......................................."""
    
    if request.method == "POST":
        userEmail = request.POST.get('email')
        userPass = request.POST.get('password')
        
        
    return render(request, "login.html")
        
    

def logout(request):
    if request.method == 'POST':
        # form = AuthenticationForm(request= request, data= request.POST)
        
        # user = form.get_user()
        auth_logout(request)
        return redirect(reverse('login'))

def noots_page(request):
    
    # template = loader.get_template('noots_page.html')
    # return HttpResponse(template.render())
    LOGED_USER_ID = request.user.id
    print(LOGED_USER_ID)
    
    context = {}
    
    varefy_user_has_value = noots.objects.filter(user_id=LOGED_USER_ID)
    if varefy_user_has_value:
        context = {
            'noots': varefy_user_has_value
        }
    return render(request, "noots_page.html", context)
    
    
    
    

def write_noots(request):
    template = loader.get_template('noots-write.html')
    return HttpResponse(template.render())



def add_or_upgrade_noots(request):
    
    LOGED_USER_ID = request.user.id
    
  
    
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
        noot_id = request.GET.get('id')
        NOOTS_TITLE = request.GET.get('title')
        NOOTS_TEXT = request.GET.get('text')
        
        if noot_id:
            nootValues = get_object_or_404(noots, id=noot_id)
            nootValues.title = NOOTS_TITLE
            nootValues.text = NOOTS_TEXT
            nootValues.save()
        else:
            # NOOTS.user_id = LOGED_USER_ID
            # NOOTS.title = NOOTS_TITLE
            # NOOTS.text = NOOTS_TEXT
            # NOOTS.save()
            
            NOOTS = noots(user_id = LOGED_USER_ID, title = NOOTS_TITLE, text=NOOTS_TEXT)
            NOOTS.save()
        
        
        # NOOTS.objects.create(
        #     title = NOOTS_TITLE,
        #     text = NOOTS_TEXT
        # )
    
    return redirect('noots-page')


def editeNoot(request, noot_id):
    #print("form editeNoot "+noot_id)
    
    noots_value = get_object_or_404(noots, id=noot_id)
    
    context = {
        'noot': noots_value
    }
    
    return render(request, 'noots-write.html', context)

def deleteNoot(request, noot_id):
    #print(noot_id)
    
    noot_to_delete = get_object_or_404(noots, id=noot_id)

    noot_to_delete.delete()
    print('noot deleted successfully')
    
    
    return redirect('noots-page')
