from django import forms
from blogs.models import Blog, Categories
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('Category_name',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('Title', 'Category', 'Image', 'Description', 'Blog_body', 'Status', 'Is_featured')

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')