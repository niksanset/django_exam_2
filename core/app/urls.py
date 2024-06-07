from django.urls import path
from app.views import MainPageView, MovieListView,SeriesListView,MovieDetailView,SearchMovieResultsView,SeriesDetailView,SearchSeriesResultsView,MovieCategoryListView,SeriesCategoryListView,login_view,logout_view,registration_view
urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('movie_list/', MovieListView.as_view(), name='movie_list'),
    path('series_list/', SeriesListView.as_view(), name='series_list'),
    path('movie_detail/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('search_movie/', SearchMovieResultsView.as_view(), name='search_movie_results'),
    path('search_series/', SearchSeriesResultsView.as_view(), name ='search_series_results'),
    path('series_detail/<int:pk>/', SeriesDetailView.as_view(), name='series_detail'),
    path('movie_category/<str:category>/', MovieCategoryListView.as_view(), name='movie_category'),
    path('series_category/<str:category>/', SeriesCategoryListView.as_view(), name='series_category'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    
    
]
