from rest_framework import serializers
from .models import User, Game, Review
class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name = 'review_detail',
        many = True,
        read_only = True
    )
    games = serializers.HyperlinkedRelatedField(
        view_name = 'game_detail',
        many = True,
        read_only = True
    )
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'photo', 'games_played', 'reviews', 'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        many = True,
        read_only = True
    )
    reviews = serializers.HyperlinkedRelatedField(
        view_name = 'review_detail',
        many = True,
        read_only = True
    )
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'rating', 'photo', 'video', 'platform', 'genre', 'release_date', 'developer', 'age_rating', 'progress', 'completed', 'still_playing', 'reviews', 'users') 


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    games = GameSerializer(
        many = True,
        read_only = True
    )
    users = UserSerializer(
        many = True,
        read_only = True
    )
    class Meta:
        model = Review
        fields = ('id', 'name', 'photo', 'body', 'rating', 'games', 'users')             

# class GameSerializer(serializers.HyperlinkedModelSerializer):
#     reviews = ReviewSerializer(
#         many = True,
#         read_only = True
#     )
#     users = UserSerializer(
#         many = True,
#         read_only = True
#     )
#     class Meta:
#         model = Game
#         fields = ('id', 'title', 'description', 'rating', 'photo', 'video', 'platform', 'genre', 'release_date', 'developer', 'age_rating', 'progress', 'completed', 'still_playing',   'reviews', 'users')

# class ReviewSerializer(serializers.HyperlinkedModelSerializer):
#     users = serializers.HyperlinkedRelatedField(
#         view_name = 'user_detail',
#         read_only = True
#     )
#     games = serializers.HyperlinkedRelatedField(
#         view_name = 'game_detail',
#         read_only = True
#     )
#     class Meta:
#         model = Review
#         fields = ('id', 'name', 'photo', 'body', 'rating', 'games', 'users')        