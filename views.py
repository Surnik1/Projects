from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def article(request):
    return HttpResponse('<h2>Main articles</h2>')
def id(request,id):
    return HttpResponse(f'<h2>ID:{id}</h2><p>"Very cool article"</p>')
def top_id(request,id):
    return HttpResponse(f'<h2>ID:{id} Comments</h2><p>1comment:Best article</p><p>2comment:Yey</p><p>3comment:i like it</p>')
def theme(request):
    category1 = request.GET.get('c1','None')
    category2 = request.GET.get('c2','None')
    return HttpResponse(f'<h2>Articles with {category1} and {category2}</h2><p>We cant find article with this theme :( </p>')

def top(request):
    return HttpResponse('<h2>TOP10 article of all time</h2><p>Top1:1</p><p>Top2:2</p><p>Top3:3</p><p>Top4:4</p>\
        <p>Top5:5</p><p>Top6:6</p><p>Top7:8</p><p>Top8:7</p><p>Top9:1111</p><p>Top10:67</p>')


def most_readible(request):
    return HttpResponse('<h2>TOP10 article of views</h2><p>Top1:19</p><p>Top2:444</p><p>Top3:3</p><p>Top4:678</p>\
        <p>Top5:566</p><p>Top6:556</p><p>Top7:4528</p><p>Top8:7777</p><p>Top9:1111</p><p>Top10:675</p>')
