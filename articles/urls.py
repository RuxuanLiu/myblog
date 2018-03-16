from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:article_title>', views.detail, name='detail'),
    path('<str:article_title>/deal_comment', views.deal_comment, name='deal_comment')
]