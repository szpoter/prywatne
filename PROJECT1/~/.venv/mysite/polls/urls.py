from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


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
    path('articles/<int:id>/like/', views.like_article, name='like_article'),
    path('articles/<int:id>/dislike/', views.dislike_article, name='dislike_article'),
    path('contact-info/', views.contact_info, name='contact_info'),
]

urlpatterns += static('/polls/photos/', document_root='polls/photos/')
urlpatterns += static('/polls/icons/', document_root='polls/icons/')