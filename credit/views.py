from django.shortcuts import render
from django.http import HttpResponse
from pardakht import handler


def index(request):
    return render(request, 'credit/index.html')

def ret():
    return HttpResponse('Res')

def buy(request):
    result = handler.create_payment(
        20000,
        'description',
        ret,
        'return_url',
        False
    )
    return HttpResponse(result['link'])
