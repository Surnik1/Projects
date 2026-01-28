from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def index(request):
    return HttpResponse('<h2>Main</h2>',headers = {'SecretCode':'8800'})
def user(request,name):
    return HttpResponse(f'<h2>Name:{name}</h2>')
def get_info(request):
    method = request.method
    path = request.path 
    user_agent = request.headers.get('User-Agent')
    host = request.get_host()

    response = HttpResponse(f"<p>Метод: {method}</p> <p>Путь: {path}</p> <p>Браузер: {user_agent}</p> <p>Хост: {host}</p>")
    response['X-Custom'] = 'No one allowed to see it'
    return response




    
