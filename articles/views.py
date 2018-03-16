from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.


def index(request):
    return HttpResponse("这是首页")


def detail(request, article_title):
    article = Article.objects.get(title=article_title)
    title = article.title
    content = article.content
    context = {'title': title, 'content': content}
    return render(request, 'articles/blog_main.html', context)


def home(request):
    article_list = Article.objects.all()
    content = {'article_list': article_list}
    return render(request, 'articles/blog_home.html', content)