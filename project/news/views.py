from django.shortcuts import render
from .models import Artiles
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

