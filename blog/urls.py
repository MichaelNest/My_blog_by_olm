from django.urls import path, include
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'), #3_ Создаем файд blog/urls.py и заполняем его - указываем что надо выполнить метод views.posts_list
# 28_Создаем имя для данного path(), чтоб по этому имени можно было б ссылаться в шаблонах html
    # path('post/<str:slug>/', post_detail, name='post_detail_url'),
# 29_ Создаем новый урл-шаблон. <str:slug> - это именнованная группа символов - в данном случае это slug типа string
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
# 53_Меняем в урл-методе поле с методом из views.py - вместо post_detail указываем PostDetail.as_view()
    path('tags/', tags_list, name='tags_list_url'),
# 38_Создаем новый урл-шаблое для тэгов
    # path('tag/<str:slug>', tag_detail, name='tag_detail_url')
# 42_Создаем урл-шаблон для перехода на страничку тегов
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail_url')
# 55_Меняем в урл-методе поле с методом из views.py - вместо post_detail указываем PostDetail.as_view()
]
