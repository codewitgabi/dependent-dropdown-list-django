from django.urls import path
from . import views


urlpatterns = [
    path("cities/", views.CityListView.as_view()),
    path("countries/", views.CountryListView.as_view())
]
