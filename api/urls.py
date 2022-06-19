from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register('articles', views.ArticleViewSet, basename="articles")
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
