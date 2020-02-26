from django.urls import path, include
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'), #3_ Создаем файд blog/urls.py и заполняем его - указываем что надо выполнить метод views.posts_list
# 28_Создаем имя для данного path(), чтоб по этому имени можно было б ссылаться в шаблонах html
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
# 29_ Создаем новый урл-шаблон. <str:slug> - это именнованная группа символов - в данном случае это slug типа string

]
