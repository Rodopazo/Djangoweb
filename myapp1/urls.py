from django.urls import path
from myapp1 import views
urlpatterns = [
    path('', views.inicio, name='Inicio')
]