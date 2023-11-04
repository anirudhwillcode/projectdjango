from django.shortcuts import render,redirect
from myapp.form import ContactForm,RegForm
from myapp.models import Contact
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    if request.user.is_authenticated:
        a=Contact.objects.filter(connect=request.user)
        return render(request,'about.html',{'obj':a})
    else:
        return render(request,'about.html')
        
def contact(request):
    x= ContactForm(request.POST)        
    if x.is_valid():
        update=x.save(commit=False)
        update.connect=request.user
        update.save()
        messages.success(request,'Data is saved to database')
        return redirect('/contact')
    return render(request,'contact.html',{'a':x})

def delete_contact(req,ID):
    a=Contact.objects.get(pk=ID)
    a.delete()
    messages.success(req,'Data is deleted from the database')
    return redirect('/about')

def update_contact(req,ID):
    data=Contact.objects.get(pk=ID)
    x=ContactForm(req.POST or None, instance=data)
    if x.is_valid():
        x.save()
        messages.success(req,'Data is saved to database')
        return redirect('/about')
    
    return render(req,'update.html',{'a':x})

def regs(req):
    x=RegForm(req.POST)
    
    if x.is_valid():
        x.save()
        return redirect('/')
    else:
        messages.error(req,'invalid credentials')
    return render(req,'register.html',{'a':x})

def login_user(req):
    if req.method=="POST":
        username=req.POST['username']
        password=req.POST['password']
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('/')
        else:
            messages.error(req,'Invalid Credentials')
        
    return render(req,'login.html')
    

def logout_user(req):
    logout(req)
    return redirect('/')