from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm

from movies.models import Movie


# Create your views here.
class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
    template_name = "movies/movie-single.html"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
