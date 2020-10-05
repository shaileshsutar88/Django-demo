from django.shortcuts import render

import random
import datetime
from datetime import date
import time
# Create your views here.

def home(request, *args, **kwargs):
    return render(request, "home.html", {})

def about(request, *args, **kwargs):
    return render(request, "about.html", {})

def password(request):
    return render(request, "password.html", {})

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


def Token(request):
    return render(request, "token.html", {})

def keepsake(request):

    token = date.today()
    token = token.strftime("%Y%m%d")
    c = int(time.time())
    c = c % 86400

    Token = str(request.GET.get('Token-Type'))
    if Token == 'Account Enquiry':
        token = str(token + 'AE' + str(c))
    elif Token == 'Cash Deposit':
        token = str(token + 'CD' + str(c))
    elif Token == 'Cash Withdrawl':
        token = str(token + 'CW' + str(c))
    elif Token == 'Cheque Submission':
        token = str(token + 'CS' + str(c))
    elif Token == 'Passbook Update':
        token = str(token + 'PU' + str(c))
    else:
        token = str(token + 'GE' + str(c))

    return render(request, "keepsake.html", {'Token_ID':token })
