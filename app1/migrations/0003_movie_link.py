# Generated by Django 5.0.1 on 2024-08-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='link',
            field=models.URLField(default='https://www.youtube.com/'),
        ),
    ]
