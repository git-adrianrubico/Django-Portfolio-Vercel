from django.urls import path
from .views import HomePageView, DigitalCVPageView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('digital_cv/', DigitalCVPageView.as_view(), name='digital_cv'),
]
