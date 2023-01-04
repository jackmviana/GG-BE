from rest_framework import serializers
from .models import User, Game, Review


# class GameSerializer(serializers.HyperlinkedModelSerializer):
#     users = serializers.HyperlinkedRelatedField(
#         view_name = 'user_detail',
#         many = True,
#         read_only = True
#     )
#     reviews = serializers.HyperlinkedRelatedField(
#         view_name = 'review_detail',
#         many = True,
#         read_only = True
#     )
#     class Meta:
#         model = Game
#         fields = ('id', 'title', 'description', 'rating', 'star_rating', 'photo', 'video', 'video_title', 'platform', 'genre', 'release_date', 'developer', 'age_rating', 'progress', 'completed', 'still_playing', 'reviews', 'users') 


# class ReviewSerializer(serializers.HyperlinkedModelSerializer):
#     games = GameSerializer(
#         many = True,
#         read_only = True
#     )
#     users = UserSerializer(
#         many = True,
#         read_only = True
#     )
#     class Meta:
#         model = Review
#         fields = ('id', 'name', 'photo', 'body', 'rating', 'games', 'users')             

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only = True
    )
    games = serializers.HyperlinkedRelatedField(
        view_name = 'game_detail',
        read_only = True
    )
    class Meta:
        model = Review
        fields = ('id', 'name', 'photo', 'body', 'rating', 'game', 'users', 'games')        

class GameSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many = True,
        read_only = True
    )
    users = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        many = True,
        read_only = True
    )
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'rating', 'star_rating', 'photo', 'gp_photo_one', 'gp_photo_two', 'gp_photo_three', 'video', 'video_title', 'color', 'platform', 'genre', 'release_date', 'developer', 'age_rating', 'progress', 'track', 'completed', 'still_playing', 'reviews', 'users') 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many = True,
        read_only = True
    )
    games = GameSerializer(
        many = True,
        read_only = True
    )
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'photo', 'games_played', 'games', 'reviews')