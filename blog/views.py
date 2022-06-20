from django.shortcuts import get_object_or_404
from .models import Article
from django.views import generic


class ArticleList(generic.ListView):
    model = Article
    context_object_name = "articles"


class ArticleDetail(generic.DetailView):
    model = Article
    slug_field = 'slug'
