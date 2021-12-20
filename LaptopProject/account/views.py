from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def RegisterView(req):
    form=UserCreationForm()
    if req.method == 'POST':
        form=UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(req,'account/register.html',context)

def LoginView(req):
    if req.method == 'POST':
        un = req.POST.get('uname')
        pw = req.POST.get('pass')

        user = authenticate(username=un,password=pw)
        if user is not None:
            login(req,user)
            return redirect('lap_show')
        else:
            print('Invalid Credentials')
            messages.error(req,'Invalid Credentials')

    return render(req,'account/login.html')

def logoutview(req):
    logout(req)
    return redirect('login')