from django.urls import path, include
from .views import CatListCreateView


urlpatterns = [
    path('cats/', CatListCreateView.as_view(), name='cats_list'),
]