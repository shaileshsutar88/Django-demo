from django.shortcuts import render

import random
# Create your views here.

def home(request, *args, **kwargs):
    return render(request, "home.html", {})

def dynamo(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    #length = 10
    length = int(request.GET.get('length'))

    wordpass = ''

    for i in range(length):
        wordpass += random.choice(characters)

    return render(request, 'dynamo.html', {'wordpass':wordpass })
