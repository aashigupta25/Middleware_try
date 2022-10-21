from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def home(request):
    print("I am Home View")
    return HttpResponse("This is Home Page")

def excp(request):
    print("I am exception View")
    a = 10/0
    return HttpResponse("This is Exception Page")

def user_info(request):
    print("I am User View")
    context = {'name': 'Aashi'}
    return TemplateResponse(request, 'blog/user.html', context)