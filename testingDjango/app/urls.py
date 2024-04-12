from django.urls import path
from .views import *

urlpatterns = [
    path('<int:element_id>/', element, name='element'),
    path('', home, name='home'),
]