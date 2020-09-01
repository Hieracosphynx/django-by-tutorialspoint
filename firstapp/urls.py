from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello, name = 'hello'),
    path('', views.index, name = 'index'),
    path('article/<articleID>', views.viewArticle, name = "article"),
    path('article/<year>/<month>', views.viewArticleMonthYear, name="articleDate"),
]

