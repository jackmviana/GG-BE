# Generated by Django 4.1.4 on 2022-12-22 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title', max_length=100)),
                ('description', models.CharField(default='no description', max_length=250)),
                ('rating', models.IntegerField()),
                ('photo', models.CharField(default='no photo', max_length=250)),
                ('video', models.CharField(default='no video', max_length=250)),
                ('platform', models.CharField(default='no platform', max_length=30)),
                ('genre', models.CharField(default='no genre', max_length=30)),
                ('release_date', models.DateField()),
                ('developer', models.CharField(default='no developer', max_length=50)),
                ('age_rating', models.CharField(default='no rating', max_length=50)),
                ('progress', models.IntegerField()),
                ('completed', models.BooleanField()),
                ('still_playing', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=200)),
                ('games_played', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('photo', models.CharField(max_length=250)),
                ('body', models.CharField(max_length=250)),
                ('rating', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='gg_app.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='gg_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='gg_app.user'),
        ),
    ]
