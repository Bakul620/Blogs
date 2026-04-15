from django.shortcuts import get_object_or_404, render

from .models import Blog, Categories

def post_by_category(request, Category_id):
    category = get_object_or_404(Categories, pk=Category_id)
    posts = Blog.objects.filter(Category_id=Category_id, Status="Published").order_by('-Created_at')

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)