from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "firstapp/index.html", {})

def hello(request):
    return render(request, "firstapp/hello.html", {})

def viewArticle(request, articleID):
    text = "The number is: %s" %articleID
    return HttpResponse(text)

def viewArticleMonthYear(request, year, month):
    text ="This is the date: %s/%s"%(year, month)
    return HttpResponse(text)