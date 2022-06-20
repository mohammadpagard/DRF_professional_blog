from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='detail'),
]
