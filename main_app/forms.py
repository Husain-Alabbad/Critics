from django.forms import ModelForm
from .models import Review
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating']


# class ProfileCreateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'gender', 'contact_number','dob' , 'image' , 'favorite_tv_show', 'favorite_novel', 'favorite_game')
#         widgets = {
#             "first_name": forms.TextInput(attrs={'class':'form-control'}),
#             "last_name": forms.TextInput(attrs={'class':'form-control'}),
#             "gender": forms.Select(choices=GENDER,attrs={'class':'form-control'}),
#             "contact_number": forms.TextInput(attrs={'class':'form-control'}),
#             "dob": forms.DateInput(attrs={'class':'form-control'}),
#             "image": forms.FileInput(attrs={'class':'form-control', "id" : "image_field"}),
#             "favorite_tv_show": forms.TextInput(attrs={'class':'form-control'}),
#             "favorite_novel": forms.TextInput(attrs={'class':'form-control'}),
#             "favorite_game": forms.TextInput(attrs={'class':'form-control'}),
#         }


# class ProfileCreateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'gender', 'contact_number','dob' , 'image' , 'favorite_tv_show', 'favorite_novel', 'favorite_game')
#         widgets = {
#             "first_name": forms.TextInput(attrs={'class':'form-control'}),
#             "last_name": forms.TextInput(attrs={'class':'form-control'}),
#             "gender": forms.Select(choices=GENDER,attrs={'class':'form-control'}),
#             "contact_number": forms.TextInput(attrs={'class':'form-control'}),
#             "dob": forms.DateInput(attrs={'class':'form-control'}),
#             "image": forms.FileInput(attrs={'class':'form-control', "id" : "image_field"}),
#             "favorite_tv_show": forms.TextInput(attrs={'class':'form-control'}),
#             "favorite_novel": forms.TextInput(attrs={'class':'form-control'}),
#             "favorite_game": forms.TextInput(attrs={'class':'form-control'}),
#         }