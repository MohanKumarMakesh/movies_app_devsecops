from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm

# Create your views here.

def sign_up(req):
    if req.method == "POST":
        form = UserSignUpForm(req.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username')
            messages.success(req, "account created for {}".format(un))
            return redirect('sign_in')
            
    elif req.method == "GET":
            form = UserSignUpForm()
    return render(req, 'users/signup.html',{'form': form})