from django.shortcuts import render
from .models import Post, Tag
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin

# Create your views here.
def posts_list(request):
    #names = ['Misha', 'Pasha', 'Sasha', 'Dasha']
    posts = Post.objects.all() # 23_Создаем переменную post - список постов из нашей модели
    return render(request, 'blog/index.html', context={'posts': posts})
    # 24_Заменяем {'names': names} на {'posts': posts}
    #5_ Возвращаем на исполнение метод render и указываем на наш шаблон index.html
    #6_ Вводим переменную context, в которой можем вносить данные в виде словаря
# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})
    # 33_ Создаем метод для перехода по кнопке Read

def tags_list(request): # 39_Создаем метод для тэгов
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

class PostDetail(ObjectDetailMixin, View): # 52_Создаем класс PostDetail, переопределяем у него метод get, вставляем в метод get содержимое из метода post_detail
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     # post = Post.objects.get(slug__iexact=slug)
    #     post = get_object_or_404(Post, slug__iexact=slug) # 56_Теперь используем метод get_object_or_404 , чтоб при обращении по несущуствующуму адресу пользователю выдавалась надпись что страница - 404
    #     return render(request, 'blog/post_detail.html', context={'post': post})

class TagDetail(ObjectDetailMixin, View): # 54_Создаем класс TagDetail, переопределяем у него метод get, вставляем в метод get содержимое из метода tag_detail
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request, slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Tag, slug__iexact=slug) # 57_Теперь используем метод get_object_or_404 , чтоб при обращении по несущуствующуму адресу пользователю выдавалась надпись что страница - 404
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})
 # 61_Импортируем класс ObjectDetailMixin и наследуемся от него в наших классах PostDetail и TagDetail
 # 62_ Убираем методы get из классов (они будут наследоваться) и определяем переменные model и template

# def tag_detail(request, slug): # 43_Создаем метод для странички тега
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag })

# >>> Post.mro() - метод mro() покажет порядок следования классов родителей.
# >>> class TagDetail(ObjectDetailMixin, View): - значит что ближайший родитель этого класса будет ObjectDetailMixin, а следующим - View
