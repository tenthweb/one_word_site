from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    message = Message.objects.first()
    return render(request, "message/home.html", {"message": message})

@login_required
def edit(request):
    message = Message.objects.first()

    if request.method == "POST":
        message.text = request.POST["text"]
        message.save()
        return redirect("home")

    return render(request, "message/edit.html", {"message": message})