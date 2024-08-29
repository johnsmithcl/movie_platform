from .models import Categories

def menu_links(request):
    links=Categories.objects.all()
    return dict(links=links)
