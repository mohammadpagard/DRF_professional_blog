from rest_framework.viewsets import ModelViewSet
from . import serializers
from blog.models import Article
from django.contrib.auth import get_user_model
from . import permissions as per


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    # Filtering for articles list
    filterset_fields = ['author', 'status']
    search_fields = [
        'title',
        'content',
        'author__username',
        'author__first_name',
        'author__last_name'
    ]
    ordering_fields = ['publish', 'updated']
    ordering = ['-publish']

    # special permission
    def get_permissions(self):
        # RetrieveAPIView for normal user
        if self.action in ['list', 'create']:
            permission_classes = [per.IsStaffOrReadOnly]
        # RetrieveUpdateDestroyAPIView and CreateAPIView for author and superuser
        else:
            permission_classes = [per.IsAuthorOrReadOnly, per.IsStaffOrReadOnly]

        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [per.IsSuperUserOrStaffReadOnly]
    # Filtering
    search_fields = [
        'username',
        'first_name',
        'last_name'
    ]
    ordering_fields = ['last_login']
    ordering = ['last_login']
