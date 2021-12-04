from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import auth

def music_emotion(request):
    return render(request,'music_emotion.html')