from django.shortcuts import render
from loginformapp.forms import user_form,user_profileform,userpostform
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from loginformapp.models import Userpost


# Create your views here.
def index(request):
    return render(request,'user_login.html')

def newpost(request):
    form = userpostform()
    if request.method == 'POST': 
        form = userpostform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('loginformapp:home'))


    return render(request,"newpost.html",{'form':form})
        
def home(request):
    images = Userpost.objects.all()   
    return render(request,"home.html",{'images':images})


def register(request):
    register=False
    if request.method=='POST':
        userform=user_form(request.POST)
        profileform=user_profileform(request.POST)

        if userform.is_valid() and profileform.is_valid():
            user= userform.save()
            user.set_password(user.password)
            user.save()

            profile =profileform.save(commit=False)
            profile.user = user # connecting the user model and our own model

            profile.save()
            register = True
    else:
        userform=user_form()
        profileform=user_profileform()
    return render(request,'registeration.html',{'userform':user_form,'profileform':profileform,'register':register})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
           
        user= authenticate(username=username, password=password)  

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('loginformapp:newpost'))
            else:
                return HttpResponse("<h1>User is not activate</h1>")
        else:
            return HttpResponse("<h1>Invalid Username or Password..!</h1>")
    return render(request,'user_login.html')

def user_logout(request):    
    logout(request)
    
    return HttpResponseRedirect(reverse('loginformapp:login'))
