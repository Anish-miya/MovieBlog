from django.shortcuts import render
from datetime import datetime
from blog.models import Article
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
#from django.urls import reverse
from django.template.response import TemplateResponse
from django.shortcuts import render
from blog.models import Article
from blog.models import Music
from blog.models import Newslatter


def index(request):
    data=Article.objects.all()
    context = {
        'current_date': datetime.now(),
        'title': 'Home'
    }
    return render(request, 'index.html',{"data":data}, context)


def about(request):
    context = {
        'current_date': datetime.now(),
        'title': 'About'
    }
    return render(request, 'about.html', context)


def components(request):
    context = {
        'current_date': datetime.now(),
        'title': 'About'
    }
    return render(request, 'components.html', context)


def news(request):
    data = Article.objects.all()
    contents= Article.content
    title=Article.title
    context = {
        'current_date': datetime.now(),
        'title': 'News'
    }
    return render(request, 'news.html', {"data":data}, context)


def song(request):
    data = Music.objects.all()
    context = {
        'current_date': datetime.now(),
        'title': 'song'
    }
    return render(request, 'song.html', {"data":data}, context)

def FB(request):

    return render(request, 'FB.html', )


def newslatter(request):

    return render(request, 'FB.html', )



'''def get_articles():
    result = Article.objects.all()
    return result


def populate_db():
    if Article.objects.count() == 0:
        Article(title='first item', content='this is the first db item').save()
        Article(title='second item', content='this is the second db item').save()
        Article(title='third item', content='this is the third db item').save()'''
