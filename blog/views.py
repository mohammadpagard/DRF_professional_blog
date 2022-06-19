from django.shortcuts import render
from .models import Article
from django.views import generic


class ArticleList(generic.ListView):
    model = Article
    context_object_name = "articles"