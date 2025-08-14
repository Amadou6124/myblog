from django.urls import path
from .views import home, ArticleCreateView


urlpatterns = [
    path('', home, name="home"),
    path('add/', ArticleCreateView.as_view(), name="article-add"),
]