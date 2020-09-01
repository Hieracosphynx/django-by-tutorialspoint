from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    today = datetime.datetime.now().date()
    return render(request, "firstapp/index.html", {"today": today})

def hello(request):
    days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    today = datetime.datetime.now().date()
    return render(request, "firstapp/hello.html", {"days": days, "date": today})

def viewArticle(request, articleID):
    text = "The number is: %s" %articleID
    return HttpResponse(text)

def viewArticleMonthYear(request, year, month):
    text ="This is the date: %s/%s"%(year, month)
    return HttpResponse(text)