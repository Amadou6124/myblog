from django.urls import path
from .views import home, ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    path('', home, name="home"),
    path('blog/', ArticleListView.as_view(), name='post-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('add/', ArticleCreateView.as_view(), name='article-add'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]