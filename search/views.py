from django.shortcuts import render
from app1.models import Movie

def search(request):
    query = request.GET.get('q')
    movies = Movie.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'movies': movies, 'query': query})
