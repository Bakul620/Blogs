
from about.models import SocialLink

from .models import Categories

def get_categories(request):
    categories = Categories.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)