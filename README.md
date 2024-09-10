Movie Platform Project

This project is a Django-based web application that allows users to register, log in, add movies, leave reviews, and explore movie details. The platform features a user-friendly interface and includes functionalities like profile management, movie categorization, and movie ratings.

Features
User Registration and Authentication: Users can register, log in, log out, and manage their profiles.
Movie Listings: Browse movies categorized by genres with pagination support.
Movie Details: Each movie has a detail page displaying the description, release date, reviews, and average rating.
Add/Edit/Delete Movies: Registered users can add, edit, and delete movies.
Review System: Users can leave reviews and rate movies on a scale of 1 to 10.
Profile Management: Users can edit their profile, including updating their bio and profile picture.
Search and Filter: Movies can be filtered by categories, and a search feature allows for easier navigation.

Technologies Used

Backend: Django (Python)
Frontend: HTML, CSS (Bootstrap), JavaScript
Database: SQLite (default)

Additional:
Django Authentication System
Slugify for URL management
UUID for unique movie identification
Getting Started
Prerequisites
Python 3.x
Django 4.x
Pillow (for handling images)


Installation

Clone the repository:
git clone https://github.com/yourusername/movie-platform.git
cd movie-platform

Create a virtual environment:
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Create a superuser for the admin panel:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the platform:
Open your browser and go to http://127.0.0.1:8000/ to view the movie platform.

Contributing
Feel free to fork this repository, make your changes, and submit a pull request. Contributions are welcome!
