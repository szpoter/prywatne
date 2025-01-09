from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('homepage')
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('homepage')
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def articles(request):
    articles_list = [
        {'id': 1, 'title': 'Kolumba Street is Open Now'},
        {'id': 2, 'title': 'Buildings Are Rising at Kępa Parnicka'},
        {'id': 3, 'title': '55m Building Rising in Pomorzany'},
        {'id': 4, 'title': 'Szczecin Goleniów Airport is Getting Renovated'},
        {'id': 5, 'title': 'New Flights and Railroad Connections from Szczecin'},
    ]
    return render(request, 'articles.html', {'articles': articles_list})

from django.shortcuts import render, get_object_or_404

def article_detail(request, id):

    article = get_object_or_404(Article, id=id)


    articles_files = {
        1: 'argument1.html',
        2: 'argument2.html',
        3: 'argument3.html',
        4: 'argument4.html',
        5: 'argument5.html',
    }

    file_name = articles_files.get(id)
    if file_name:
        return render(request, f'articles/{file_name}', {'article': article, 'id': id})
    else:
        return HttpResponse("<h1>Article not found</h1>", status=404)

    
from django.shortcuts import render, get_object_or_404
from .models import Article

def about_us(request):
    return render(request, 'about_us.html')

def news_from_szczecin(request):
    return render(request, 'news_from_szczecin.html')

def contact_info(request):
    return render(request, 'contact_info.html')

def search_article(request):
    query = request.GET.get('query', '')
    articles = Article.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_results.html', {'articles': articles, 'query': query})

def homepage(request):
    return render(request, 'homepage.html')

from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('login')

from django.shortcuts import get_object_or_404, redirect
from .models import Article

def like_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user.is_authenticated:
        if request.user in article.dislikes.all():
            article.dislikes.remove(request.user)  
        if request.user not in article.likes.all():
            article.likes.add(request.user)
        else:
            article.likes.remove(request.user)
    return redirect('article_detail', id=id)

def dislike_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user.is_authenticated:
        if request.user in article.likes.all():
            article.likes.remove(request.user) 
        if request.user not in article.dislikes.all():
            article.dislikes.add(request.user) 
        else:
            article.dislikes.remove(request.user)  
    return redirect('article_detail', id=id)
