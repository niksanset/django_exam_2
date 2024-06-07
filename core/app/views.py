from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView
from app.models import Movie, TVShow
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User





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
    
    
class MovieCategoryListView(ListView):
    model = Movie
    template_name = 'app/movie_category.html'
    context_object_name = 'movie_list'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.kwargs['category']
        if category.lower() == 'all':
            return queryset.order_by('-year')
        else:
            return queryset.filter(genres__icontains=category).order_by('-year')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']  
        return context


class SeriesCategoryListView(ListView):
    model = TVShow
    template_name = 'app/series_category.html'
    context_object_name = 'series_list'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.kwargs['category']
        if category.lower() == 'all':
            return queryset.order_by('-premiered')
        else:
            return queryset.filter(genres__icontains=category).order_by('-premiered')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']  
        return context
        
    
class SeriesListView(ListView):
    model = TVShow
    template_name = 'app/series_list.html'
    context_object_name = 'series_list'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-premiered')  



class MovieDetailView(DetailView):
    model = Movie
    template_name = 'app/movie_detail.html'
    context_object_name = 'movie_detail'
    


class SeriesDetailView(DetailView):
    model = TVShow
    template_name = 'app/series_detail.html'
    context_object_name = 'series_detail'
    
    


class SearchMovieResultsView(ListView):
    template_name = 'app/search_movie_results.html'
    context_object_name = 'results'
  

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            movie_results = Movie.objects.filter(title__icontains=query)
            
        else:
            movie_results = []
        return movie_results
    
    
class SearchSeriesResultsView(ListView):
    template_name = 'app/search_series_results.html'
    context_object_name = 'results'
    
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            series_results = TVShow.objects.filter(name__icontains=query)
            
        else:
            series_results = []
        return series_results
    
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')  
        else:
       
            error_message = "Invalid username or password. Please try again."
            return render(request, 'app/login.html', {'error_message': error_message})
    else:
        return render(request, 'app/login.html')

def logout_view(request):
    logout(request)
    return redirect('main_page')


def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            error_message = "Passwords do not match. Please try again."
            return render(request, 'app/registration.html', {'error_message': error_message})
        user = User.objects.create_user(username=username, email=email, password=password1)
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'app/registration.html', {'error_message': error_message})
    else:
        return render(request, 'app/registration.html')