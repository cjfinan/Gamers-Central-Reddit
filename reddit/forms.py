from .models import Comment, Post, UserProfile
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'content', 'featured_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditUserProfileForm(UserChangeForm):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    email = forms.EmailField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    # is_superuser = forms.CharField(
    #     max_length=100, widget=forms.CheckboxInput(
    #         attrs={'class': 'form-check'}))
    # is_staff = forms.CharField(
    #     max_length=100, widget=forms.CheckboxInput(
    #         attrs={'class': 'form-check'}))
    # date_joined = forms.CharField(
    #     max_length=100, widget=forms.TextInput(
    #         attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_picture', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            # 'profile_picture': forms.TextInput(
            #     max_length=100, widget=forms.TextInput(
            #         attrs={'class': 'form-control'})),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
