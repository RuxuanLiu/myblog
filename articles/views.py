from django.shortcuts import render, get_object_or_404, _get_queryset
from django.http import HttpResponse
from .models import Article
from markdown import markdown
# Create your views here.


def index(request):
    return HttpResponse("这是首页")


def detail(request, article_title):
    article = get_object_or_404(Article, title =article_title)
    title = article.title
    content_render_by_markdown = markdown(article.content, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    context = {'title': title, 'content': content_render_by_markdown}
    return render(request, 'articles/blog_main.html', context)


def home(request):
    article_list = _get_queryset(Article)
    content = {'article_list': article_list}
    return render(request, 'articles/blog_home.html', content)