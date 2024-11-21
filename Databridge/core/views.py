from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request,"core/index.html")


def logout(request):
    logout(request)
    return redirect("home")

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        return render(request,"core/login.html",{
            "form":form,
        })


    