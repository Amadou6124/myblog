from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Article
 


# Create your views here.
def home(request):
    articles = Article.objects.order_by('-created_at')[:6]  
    return render(request, 'post/index.html', {'articles': articles})

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'image']
    template_name = 'post/article_create.html'
    success_url = reverse_lazy('home')