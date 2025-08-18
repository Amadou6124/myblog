from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Article

 


# Create your views here.
def home(request):
    articles = Article.objects.order_by('-created_at')[:9]  
    return render(request, 'post/index.html', {'articles': articles})


class ArticleListView(ListView):
    model = Article
    template_name = 'post/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(title__icontains=query)
        return Article.objects.all()
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'post/article_detail.html'
    context_object_name = 'articles'


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'image']
    template_name = 'post/article_create.html'
    success_url = reverse_lazy('home')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'image']
    template_name = 'post/article_form.html'
    success_url = reverse_lazy('home')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'post/article_confirm_delete.html'
    success_url = reverse_lazy('home')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'post/contact.html', {'form': form})