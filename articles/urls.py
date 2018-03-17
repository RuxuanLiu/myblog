from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse

app_name = 'articles'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('<str:article_title>/', views.detail, name='detail'),
    path('<str:article_title>/deal_comment/', views.deal_comment, name='deal_comment')
]