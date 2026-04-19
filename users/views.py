from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == "GET":
        pass
    else:
        print(request.POST)
    return render(request, "signup.html", {"form": UserCreationForm})
