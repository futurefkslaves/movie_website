from django.urls import path
from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='single_view'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review')
]
