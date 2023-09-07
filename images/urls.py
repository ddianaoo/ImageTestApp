from django.urls import path, include
from .views import ImageListCreateView

# router = DefaultRouter()
# router.register(r'images', ImageListCreateView)

urlpatterns = [
    path('images/', ImageListCreateView.as_view(), name='images_list'),
]