from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by("date")
    context ={
        "articles":articles,
    }
    return render(request,'article/article.html',context)

def article_detail(request,slug):
    return HttpResponse(slug)