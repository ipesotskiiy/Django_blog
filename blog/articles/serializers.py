from datetime import datetime

from rest_framework import serializers

from articles.models import Article, Genre


class ReadArticleSerializer(serializers.ModelSerializer):
    article_id = serializers.SerializerMethodField('get_id')

    class Meta:
        depth = 1
        model = Article
        fields = (
            '__all__'
        )

    def get_id(self, obj):
        return obj.id


class WriteAndUpdateArticleSerializer(serializers.ModelSerializer):
    article_id = serializers.SerializerMethodField('get_id')
    login = serializers.ReadOnlyField(source='user.login')
    publication_date = serializers.DateTimeField(default=datetime.now())

    class Meta:
        depth = 1
        model = Article
        fields = (
            'login',
            'article_id',
            'user_id',
            'title',
            'text',
            'publication_date',
        )

    def get_id(self, obj):
        return obj.id




class GenreSerializer(serializers.ModelSerializer):
    genre_id = serializers.SerializerMethodField('get_id')

    class Meta:
        model = Genre
        fields = ('name',
                  'genre_id')

    def get_id(self, obj):
        return obj.id