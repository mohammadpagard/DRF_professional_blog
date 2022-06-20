from rest_framework.viewsets import ModelViewSet
from . import serializers
from blog.models import Article
from django.contrib.auth import get_user_model
from . import permissions as per
from rest_framework import permissions


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [per.IsStaffOrReadOnly]
        else:
            permission_classes = [per.IsAuthorOrReadOnly, per.IsStaffOrReadOnly]

        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [per.IsSuperUserOrStaffReadOnly]
