from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden
# Create your views here.
data = {
    "Кофе в зернах": 850,
    "Чай листовой": 420,
    "Ароматическая свеча": 600,
    "Кружка керамическая": 450,
    "Плед шерстяной": 2200,
    "Блокнот в точку": 350,
    "Ручка гелевая": 120,
    "Термос": 1100,
    "Суккулент": 300,
    "Шоколад ремесленный": 280,
    "Набор стикеров": 150,
    "Зеркало настольное": 950,
    "Носки с принтом": 250,
    "Ланч-бокс": 750,
    "Коврик для йоги": 1800,
    "Эспандер": 400,
    "Книга": 650,
    "Закладка для книг": 80,
    "Настольная лампа": 1600,
    "Гирлянда": 500,
    "Увлажнитель воздуха": 2100,
    "Подставка под ноутбук": 1300,
    "Зонт-автомат": 1200,
    "Шоппер": 400,
    "Тапочки": 900
}
def home(request):
    return HttpResponse('<h2>HomePage</h2>')
def tocontactus(request):
    return redirect('/contact-us/')
def contactus(request):
    return HttpResponse('<h2>Our contacts:</h2>')
def products(request):
    return JsonResponse(data)
def set_cookie(request,name,id):
    response = HttpResponse("Cookie установлена")
    response.set_cookie(name, id, max_age=3600) # Cookie будет действительна 1 чаc
    return response
