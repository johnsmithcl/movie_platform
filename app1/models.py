from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
import uuid
class User_reg(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    release_date = models.DateField()
    category = models.ForeignKey(Categories, related_name='movies', on_delete=models.CASCADE)
    added_by = models.ForeignKey(User_reg, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    rating = models.FloatField(default=0.0)
    link = models.URLField(default='https://www.youtube.com/')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + '-' + str(uuid.uuid4()))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ReviewRatings(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User_reg, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    review = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'

    def average_rating(self):
        reviews = ReviewRatings.objects.filter(movie=self.movie)
        avg = reviews.aggregate(models.Avg('rating'))['rating__avg']
        return avg if avg else 0
