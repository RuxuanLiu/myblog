from django.contrib import admin
from articles.models import Article, Tag, Comment


# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Comment)