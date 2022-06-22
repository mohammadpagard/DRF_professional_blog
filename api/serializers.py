from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


class ArticleSerializer(serializers.ModelSerializer):
    def get_author(self, obj):
        return [
            obj.author.username,
            obj.author.first_name,
            obj.author.last_name,
        ]

    author = serializers.SerializerMethodField("get_author")

    class Meta:
        model = Article
        exclude = ['created', 'updated']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
