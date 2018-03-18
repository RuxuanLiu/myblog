from django.shortcuts import render, get_object_or_404, get_list_or_404, _get_queryset
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Comment, Tag
from .models import RelationOfArticleAndTag as RAT
from markdown import markdown
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
# Create your views here.


def index(request):
    return HttpResponse("这是首页")


def detail(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    RAT_list = RAT.objects.filter(article__title='Hello World')
    article_tag_list = [obj.tag for obj in RAT_list ]
    comment_list = Comment.objects.filter(article__title=article_title)

    content_render_by_markdown = markdown(article.content, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])

    context = {'article': article, 'content': content_render_by_markdown, 'comment_list': comment_list,
               'tag_list': tag_list(), 'article_tag_list': article_tag_list}
    return render(request, 'articles/blog_main.html', context)


def home(request):
    article_list = _get_queryset(Article)
    content = {'article_list': article_list, 'tag_list': tag_list()}
    return render(request, 'articles/blog_home.html', content)


@login_required
def deal_comment(request, article_title):
    article = get_object_or_404(Article, title=article_title)
    comment_context = request.POST['comment']
    comment = Comment.objects.create(article=article, context=comment_context, author=request.user.username)
    comment.save()
    return HttpResponseRedirect(reverse('articles:detail', args=(article_title,)))


def tag_list():
    tag_list = Tag.objects.all()
    return tag_list
