from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Article
 


# Create your views here.
def home(request):
    return render(request, 'post/index.html')

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'image']
    template_name = 'post/article_create.html'
    success_url = reverse_lazy('home')