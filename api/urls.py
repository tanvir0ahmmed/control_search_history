from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('search-list/',views.search_list),
    path('smartphone-list/',views.smartphone_list),
]
