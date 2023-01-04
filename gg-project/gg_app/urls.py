from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>', views.GameDetail.as_view(), name='game-detail'),
    path('trackerupdate/<int:pk>', views.GameUpdate.as_view(), name='game_detail'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    path('reviewspost/', views.ReviewPost.as_view(), name='review_detail'),
    path('reviewsupdate/<int:pk>', views.ReviewUpdate.as_view(), name='review_detail'),
    path('reviewsdelete/<int:pk>', views.ReviewDelete.as_view(), name='review_detail'),
]