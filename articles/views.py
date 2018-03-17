from django.shortcuts import render, get_object_or_404, _get_queryset
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Comment
from markdown import markdown
from django.urls import reverse
# Create your views here.


def index(request):
    return HttpResponse("这是首页")


def detail(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    title = article.title
    comment_list = Comment.objects.filter(article__title=article_title)
    content_render_by_markdown = markdown(article.content, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    context = {'title': title, 'content': content_render_by_markdown, 'comment_list': comment_list}
    return render(request, 'articles/blog_main.html', context)


def home(request):
    article_list = _get_queryset(Article)
    content = {'article_list': article_list}
    return render(request, 'articles/blog_home.html', content)


def deal_comment(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    comment_context = request.POST['comment']
    comment_author = request.POST['author']
    comment = Comment.objects.create(article=article, context=comment_context, author=comment_author)
    comment.save()
    return HttpResponseRedirect(reverse('articles:detail', args=(article_title,)))
