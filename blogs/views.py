from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Categories

def post_by_category(request, Category_id):
    # Logic to retrieve posts based on the Category_id
    # For example, you might query the Blog model to get posts in that category
    posts = Blog.objects.filter(Category_id=Category_id, Status="Published").order_by('-Created_at')
    try:
        # Retrieve the category name based on the Category_id
        category = Categories.objects.get(pk=Category_id)
    except:
        # If the category does not exist, you can handle it as needed (e.g., show an error message or redirect)
        return redirect('home')

    # category = get_object_or_404(Categories, pk=Category_id)

        
    context = {
        'posts': posts,
        'category':category
    }
    return render(request, 'post_by_category.html', context)