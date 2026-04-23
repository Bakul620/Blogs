from django import forms
from blogs.models import Blog, Categories

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields ='__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('Title', 'Category', 'Image', 'Description', 'Blog_body', 'Status', 'Is_featured')