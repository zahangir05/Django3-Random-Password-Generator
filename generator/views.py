from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def home(request):
    # return HttpResponse('Hello World from Django 3 - Password Generator!!..')
    return render(request, 'home.html')


def aboutPassGen(request):
    return render(request, 'about.html')


def generatePassword(request):
    finalPassword = ''
    charList = list('abcdefghijklmnopqrstuvwxyz')

    if (request.GET.get('upperCase')):
        charList.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if (request.GET.get('number')):
        charList.extend(string.digits)

    if (request.GET.get('specialChar')):
        charList.extend(string.punctuation)

    for x in range(int(request.GET.get('length', 8))):  # Default length has been considered as 8
        finalPassword += random.choice(charList)
    return render(request, 'password.html', {'password': finalPassword})
