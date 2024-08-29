from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, EditProfileForm
from .models import Movie, ReviewRatings, Categories
from django.core.paginator import Paginator
from django.db.models import Avg
from .forms import ReviewForm
from .forms import MovieForm
import uuid
from django.utils.text import slugify

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log in the user after successful registration
            messages.success(request, f'Registration successful! Welcome, {user.username}!')
            return redirect('app1:login')
        else:
            messages.error(request, 'There were errors in your registration form. Please correct them.')
    else:
        form = UserForm()

    return render(request, 'registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('app1:home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('app1:login')

@login_required
def view_profile(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('app1:view_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})

def movie_list(request):
    """
    View to display a list of all movies, possibly with filtering by category, and includes pagination.
    """
    category_slug = request.GET.get('category')
    category = None
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        movies = Movie.objects.filter(category=category)
    else:
        movies = Movie.objects.all()

    # Implement pagination
    paginator = Paginator(movies, 10)  # Show 10 movies per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Fetch all categories to display in the filter
    categories = Categories.objects.all()

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category,
    }

    return render(request, 'home.html', context)

def movie_detail(request, c_slug, m_slug):
    """
    View to display the detail of a single movie.
    """
    movie = get_object_or_404(Movie, slug=m_slug, category__slug=c_slug)
    reviews = ReviewRatings.objects.filter(movie=movie)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']  # Calculate the average rating

    context = {
        'movie': movie,
        'reviews': reviews,
        'average_rating': average_rating,
    }
    return render(request, 'movie_detail.html', context)

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user  # Set the added_by field to the logged-in user
            movie.save()
            return redirect('app1:movie_list')  # Redirect to a success page or movie list
    else:
        form = MovieForm()
    return render(request, 'add_movies.html', {'form': form})

@login_required
def edit_movie(request, c_slug, m_slug):
    movie = get_object_or_404(Movie, slug=m_slug, category__slug=c_slug)  # Also filter by category slug
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie updated successfully!')
            return redirect('app1:movie_detail', c_slug=c_slug, m_slug=movie.slug)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'edit_movie.html', {'form': form, 'movie': movie})
@login_required
def delete_movie(request, c_slug, m_slug):
    """
    View to delete a movie.
    """
    movie = get_object_or_404(Movie, slug=m_slug, category__slug=c_slug)
    if request.method == 'POST':
        movie.delete()
        messages.success(request, 'Movie deleted successfully!')
        return redirect('app1:movie_list')
    return render(request, 'delete.html', {'movie': movie})


@login_required

def add_review(request, c_slug, m_slug):
    """
    View to add a review for a movie.
    """
    movie = get_object_or_404(Movie, slug=m_slug, category__slug=c_slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Save the review but don't commit to the database yet
            review = form.save(commit=False)
            review.user = request.user  # Set the current user as the reviewer
            review.movie = movie  # Associate the review with the movie
            review.save()

            messages.success(request, 'Your review has been added successfully!')
            return redirect('app1:movie_detail', c_slug=movie.category.slug, m_slug=movie.slug)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'movie': movie, 'form': form})

