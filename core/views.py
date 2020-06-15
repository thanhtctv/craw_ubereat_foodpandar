from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from bs4 import BeautifulSoup
from django.shortcuts import redirect
import requests
import urllib.request
import json




# Create your views here.


def index(request):
        return render(request,'homepage/index.html')


def search(request):
        return render(request,'homepage/result.html')


def vote(request):
    # choiceclass = request.POST["choiceclass"]
    # choicecountry = request.POST["choicecountry"]
    # search = request.POST['search']
    res = requests.get("https://www.foodpanda.com.tw/restaurants/new?lat=24.178824&lng=120.6466926&vertical=restaurants")

    soup = BeautifulSoup(res.text, 'html.parser')

    tag_name = "section.vendor-lane-section h3.title-flat"
    articles = soup.select(tag_name)
    tag_name = "div.lane-wrapper ul.vendor-lane li a"
    articles = soup.select(tag_name)
    return HttpResponse(articles)
    lis = []
    count = 0
    for art in articles:
        #return HttpResponse(art)
        dic = {'href': 'https://www.foodpanda.com.tw/' + art['href'],
               'img': art.select("picture div")[0]['data-src'].split("|")[0],
               'name': art.select("span.name.fn")[0].text,
               'delivering time': art.select("span.badge-info")[0].text.replace(" ", "").replace("\n", "")}
        lis.append(dic)

    return render(request,'homepage/result.html',{"q":lis})
