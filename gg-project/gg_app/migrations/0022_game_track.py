# Generated by Django 4.1.4 on 2023-01-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gg_app', '0021_game_gp_photo_one_game_gp_photo_three_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='track',
            field=models.CharField(default='not tracked', max_length=50),
        ),
    ]
