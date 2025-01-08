from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:id>/', views.article_detail, name='article_detail'),
    path('about-us/', views.about_us, name='about_us'),
    path('news-from-szczecin/', views.news_from_szczecin, name='news_from_szczecin'),
    path('contact-info/', views.contact_info, name='contact_info'),
    path('search-article/', views.search_article, name='search_article'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.logout_user, name='logout'),
]
