from django.shortcuts import render
from .models import Post, Tag

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

def tags_list(request): # 39_Создаем метод для тэгов
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

def tag_detail(request, slug): # 43_Создаем метод для странички тега
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag })
