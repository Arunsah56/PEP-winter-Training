from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    return render(request, "index.html")

def post_detail(request, slug):
    POST = get_object_or_404(Post, slug=slug)
    return render(request, "post_detail.html", {"POST": POST})

def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})
    