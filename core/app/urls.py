from django.urls import path
from app.views import MainPageView, MovieListView,SeriesListView
urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('movie_list/', MovieListView.as_view(), name='movie_list'),
    path('series_list/', SeriesListView.as_view(), name='series_list'),
]
