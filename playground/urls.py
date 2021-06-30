from django.urls import path, include
from . import views

# url config
urlpatterns = [
    path('hello/', views.say_hello)
]


