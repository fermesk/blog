from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by("date")
    context ={
        "articles":articles,
    }
    return render(request,'article/article.html',context)

def article_detail(request,slug):
    article_list = Article.objects.get(slug=slug)
    context = {
       "article_list":article_list, 
    }

    return render(request,'article/article_detail.html',context)

@login_required(login_url="/account/signin/")
def create(request):
    return render(request,'article/create.html')