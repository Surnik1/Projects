from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(rrequet):
    return HttpResponse('<h2>Main page of shop!</h2><h2>to see our products write p</h2>')
def contact(request):
    return HttpResponse('Contact: 87784914462')
def about(request):
    return HttpResponse('Site of unreal products')
def products(request):
    return HttpResponse('<h2>Our Products:</h2><h2>1:Tablet</h2><h2>2:Phone</h2>') 
def tablet(request):
    return HttpResponse('<h2>Our Tablets:</h2><h2>Unfortunately,they was sold out</h2>') 
def phone(request):
    return HttpResponse('<h2>Our Phones:</h2><h2>Unfortunately,they was sold out</h2>') 
def user(request,name):
    return HttpResponse(f'<h2>User</h2>Name:{name}')