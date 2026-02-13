from django.shortcuts import render, get_object_or_404
from .models import Article
from django.views.generic import ListView, DetailView   
# Create your views here.

    

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"