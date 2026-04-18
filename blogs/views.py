from django.shortcuts import get_object_or_404, render

from .models import Blog, Categories
from django.db.models import Q

def post_by_category(request, Category_id):
    category = get_object_or_404(Categories, pk=Category_id)
    posts = Blog.objects.filter(Category_id=Category_id, Status="Published").order_by('-Created_at')


    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)

def blog_detail(request, slug):
    single_blog = get_object_or_404(Blog, Slug=slug, Status="Published")
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blog_detail.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(Title__icontains=keyword) | Q(Description__icontains=keyword) | Q(Blog_body__icontains=keyword), Status="Published")
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)