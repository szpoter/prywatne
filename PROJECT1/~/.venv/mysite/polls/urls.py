from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:id>/', views.article_detail, name='article_detail'),
]