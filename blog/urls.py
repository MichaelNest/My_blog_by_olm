from django.urls import path, include
from .views import *

urlpatterns = [
    path('', posts_list) #3_ Создаем файд blog/urls.py и заполняем его - указываем что надо выполнить метод views.posts_list
]
