from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random


   
def index(request):
    if 'x' not in request.session:
        request.session['x'] = 0
    
    if 'list' not in request.session:
        request.session['list'] = []
    
    
    return render(request,"first_app/index.html")

    
def count(request):
    
    if request.session['x'] == "No money, No play!":
        return redirect('/')
    
    if request.POST['building'] == 'farm':
        num = random.randint(10,20)
        request.session['x'] += num
        
    elif request.POST['building'] == 'cave':
        num = random.randint(5,10)
        request.session['x'] += num
       
    elif request.POST['building'] == 'house':
        num = random.randint(2,5)
        request.session['x'] += num
    
    elif request.POST['building'] == 'casino':
        if request.session['x'] <= 0:
          request.session['x'] = "No money, No play!"
          return redirect('/')
        elif request.session['x'] > 0:
          num = random.randint(-50,50)
          request.session['x'] += num
    
    if num >= 0:
        request.session['list'].append( "<li class='black'> You earned " + str(num) + " Gold " + strftime("%Y-%m-%d %H:%M %p", gmtime())+ "</li>")
        
    else:
        request.session['list'].append( "<li class= 'red'> Oops you lost " + str(num) + " Gold " + strftime('%Y-%m-%d %H:%M %p', gmtime())+ "</li>")
    request.session['list'].reverse()
    return redirect("/")


       
def reset(request):
    request.session.clear()
    return redirect("/")

