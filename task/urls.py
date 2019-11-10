from django.urls import path

from .views import *

urlpatterns = [
    path('task/', text_area),
    path('', index_page),
]
