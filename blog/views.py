from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    #names = ['Misha', 'Pasha', 'Sasha', 'Dasha']
    posts = Post.objects.all() # 23_Создаем переменную post - список постов из нашей модели
    return render(request, 'blog/index.html', context={'posts': posts})
    # 24_Заменяем {'names': names} на {'posts': posts}
    #5_ Возвращаем на исполнение метод render и указываем на наш шаблон index.html
    #6_ Вводим переменную context, в которой можем вносить данные в виде словаря
def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})
    # 33_ Создаем метод для перехода по кнопке Read
