from django.urls import path
from .views import DietaryOptionList, DietaryOptionDetail

urlpatterns = [
    path('dietary-options/', DietaryOptionList.as_view(), name='dietaryoption-list'),
    path('dietary-options/<int:pk>/', DietaryOptionDetail.as_view(), name='dietaryoption-detail'),
]
