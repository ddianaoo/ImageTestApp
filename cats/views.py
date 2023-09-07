from rest_framework import generics
from .models import Cat
from .serializers import CatSerializer


class CatListCreateView(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
