from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

# Create your views here.
def registration(request):
    form = SignupForm(request.POST)
    context = {
        'form':form
    }
    return render(request, 'registration/registration.html', context)

def create_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    #We're to redirect to login page
    return redirect("/login")    
                