from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(requests):
    return HttpResponse('Welcome to eMobilis!')


def about(requests):
    return HttpResponse('About eMobilis')


def contact(requests):
    return HttpResponse('Mobile: 00254123456789 <p> Email: emobilis@abc.com')


def services(requests):
    return HttpResponse('Courses <br> Bootcamps <br> Web Development')


def learn(requests):
    return HttpResponse('View our courses <p> Get a quote <p> Register')
