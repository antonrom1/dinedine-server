from rest_framework import generics
from .models import DietaryOption
from .serializers import DietaryOptionSerializer


class DietaryOptionList(generics.ListCreateAPIView):
    queryset = DietaryOption.objects.all()
    serializer_class = DietaryOptionSerializer


class DietaryOptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DietaryOption.objects.all()
    serializer_class = DietaryOptionSerializer
