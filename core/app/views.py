from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView
from app.models import Movie, TVShow
class MainPageView(TemplateView):
    template_name = 'app/main_page.html'
    
    
class MovieListView(ListView):
    model = Movie
    template_name = 'app/movie_list.html'
    context_object_name = 'movie_list'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-year')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
class SeriesListView(ListView):
    model = TVShow
    template_name = 'app/series_list.html'
    context_object_name = 'series_list'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-premiered')  

   