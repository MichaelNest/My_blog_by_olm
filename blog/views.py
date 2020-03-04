from django.shortcuts import render
from .models import Post, Tag
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import *
from .forms import TagForm, PostForm
from django.shortcuts import redirect

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
class PostCreate(ObjectCreateMixin, View): # 81_Создаем метод get класса TagCreate
    model_form = PostForm
    template = 'blog/post_create_form.html'
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create_form.html', context={'form': form})
    #
    # def post(self, request): # 82_Создаем метод post в классе TagCreate, проверяем валидность введенной информации
    #     bound_form= PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create_form.html', context={'form':bound_form})
class PostUpdate(ObjectUpdateMixin, View): # 92_Создаем class PostUpdate(ObjectUpdateMixin, View)
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'

class PostDelete(ObjectDeleteMixin, View): # 100_Создаем class PostDelete(ObjectUpdateMixin, View) (blog/views.py)
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'

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

class TagCreate(ObjectCreateMixin, View): #86_Переносим класс TagCreate из blog/views.py в blog/utils.py и делаем Миксин
    model_form = TagForm
    template = 'blog/tag_create.html'
#     def get(self, request):# 69_Создаем метод get класса TagCreate
#         form = TagForm()
#         return render(request, 'blog/tag_create.html', context={'form': formW})
#
#     def post(self, request): # 74_Создаем метод post в классе TagCreate, проверяем валидность введенной информации
#         bound_form = TagForm(request.POST)
#
#         if bound_form.is_valid():
#             new_tag= bound_form.save()
#             return redirect(new_tag)
#         return render(request, 'blog/tags_list.html', context={'form': bound_form})

class TagUpdate(ObjectUpdateMixin, View): #87 Создаем класс для изменения тэгов - class TagUpdate(View) - создаем методы get и post
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form':bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag=Tag.objects.get(slug__iexist=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #     if bound_form.is_valid:
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_update_form', context={'form':bound_form, 'tag': tag})
class TagDelete(ObjectDeleteMixin, View): # 95_Создаем класс для удаления тегов, в нем реализуем два метода - get и post
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/tag_delete_form.html', context={'tag':tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))# 'tags_list_url' - имя из списка урлов blog/urls.py
# >>> Post.mro() - метод mro() покажет порядок следования классов родителей.
# >>> class TagDetail(ObjectDetailMixin, View): - значит что ближайший родитель этого класса будет ObjectDetailMixin, а следующим - View
