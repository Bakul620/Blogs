from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    Category_name = models.CharField(max_length=50, unique=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.Category_name

STATUS_CHOICES = (
    ("Draft", 'Draft'),
    ("Published", 'Published'),
)
class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=500)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    Slug = models.SlugField(max_length=150, unique=True,blank=True)
    Blog_body = models.TextField(max_length=2000)
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    Is_featured = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
   