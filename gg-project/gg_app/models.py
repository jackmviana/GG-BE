from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    photo = models.CharField(max_length=200)
    games_played = models.CharField(max_length=40)

    def __str__(self):
        return self.username 

class Game(models.Model):
    title = models.CharField(max_length=100, default='no title')
    description = models.CharField(max_length=1000, default='no description')
    rating = models.IntegerField()
    star_rating = models.IntegerField(default=1)
    photo = models.CharField(max_length=250, default='no photo')
    gp_photo_one = models.CharField(max_length=250, default='no photo')
    gp_photo_two = models.CharField(max_length=250, default='no photo')
    gp_photo_three = models.CharField(max_length=250, default='no photo')
    video = models.CharField(max_length=250, default='no video')
    video_title = models.CharField(max_length=250, default='no video title')
    color = models.CharField(max_length=250, default='no color')
    platform = models.CharField(max_length=100, default='no platform')
    genre = models.CharField(max_length=100, default='no genre')
    release_date = models.DateField()
    developer = models.CharField(max_length=50, default='no developer')
    age_rating = models.CharField(max_length=50, default='no rating')
    progress = models.IntegerField()
    track = models.CharField(max_length=50, default='not tracked')
    completed = models.BooleanField()
    still_playing = models.BooleanField()
    user = models.ManyToManyField(User, related_name="user")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return self.title 

class Review(models.Model):
    name = models.CharField(max_length=250, default="no name", null=True)
    photo = models.CharField(max_length=250, default="no photo", null=True)
    body = models.CharField(max_length=250, default="no body", null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews', null=True)

    def __str__(self):
        return self.name 