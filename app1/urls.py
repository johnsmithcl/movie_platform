from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # Profile
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    # Landing and Home
    path('', views.landing_page, name='landing'),           # Public landing page
    path('home/', views.movie_list, name='home'),           # Login-required movie list page

    # Movies
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/add/', views.add_movie, name='add_movie'),
    path('movies/<slug:c_slug>/<slug:m_slug>/', views.movie_detail, name='movie_detail'),
    path('movies/<slug:c_slug>/<slug:m_slug>/edit/', views.edit_movie, name='edit_movie'),
    path('<slug:c_slug>/<slug:m_slug>/delete/', views.delete_movie, name='delete_movie'),
    path('movie/<slug:c_slug>/<slug:m_slug>/add-review/', views.add_review, name='add_review'),
    path('recommendations/', views.personalized_recommendations, name='recommendations'),
]
