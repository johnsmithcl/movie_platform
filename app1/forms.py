from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User_reg, Movie, ReviewRatings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User_reg
        fields = ['username', 'email', 'bio', 'profile_pic']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'category', 'poster','link']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRatings
        fields = ['rating', 'review']
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User_reg
        fields = ('first_name', 'last_name', 'email', 'bio', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # Customize the form fields if needed
        self.fields['bio'].widget = forms.Textarea(attrs={'rows': 3})