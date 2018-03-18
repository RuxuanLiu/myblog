from django.contrib import admin
from articles.models import Article, Tag, Comment, RelationOfArticleAndTag


# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(RelationOfArticleAndTag)
