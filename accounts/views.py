#from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.

def Welcome(request):
    welcome_message = render_to_string('accounts/signup_Welcome.txt', {
    'name' : '김범수',
    'when' : '2019년 7월 23일',
    })
    return HttpResponse(welcome_message)