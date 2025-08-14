from django.urls import path
from .views import home, ArticleListView, ArticleCreateView


urlpatterns = [
    path('', home, name="home"),
    path('blog/', ArticleListView.as_view(), name='post-list'),
    path('add/', ArticleCreateView.as_view(), name="article-add"),
]