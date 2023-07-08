from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('event/', event),
    path('contact/', contact),
    path('menu/', menu),
    path('about/', about),
    path('index/', index)
]