from django.shortcuts import render
from .models import Post, Tag
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import *
from .forms import TagForm, PostForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin # 122_Импортируем класс LoginRequiredMixin и вставляем его как ближайшего родителя в наши классы, доступ к которым мы хотим ограничить
from django.core.paginator import Paginator
from django.db.models import Q # 143_Импортируем класс Q - для работы поисковика

# Create your views here.
def posts_list(request):
    #names = ['Misha', 'Pasha', 'Sasha', 'Dasha']
    search_query = request.GET.get('search', '') # 141_Создаем переменную для поиска search_query, прописываем в ней ключ 'search', определим в шаблоне base.html в форме для поисковика
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        # 143_Формируем поиск по титлу и по телу поста через класс Q - поиск работал корректно
    else:
        posts = Post.objects.all() # 23_Создаем переменную post - список постов из нашей модели

    paginator = Paginator(posts, 2) # 127_Импортируем класс Paginator и создаем в методе post_list обьект paginator, указываем модель posts и количества постов на страничке


    page_number = request.GET.get('page', 1) # 130_Создаем переменную page_number - номер страници. Извлекаем его из словаря GET обьекта request по ключу 'page'. Значение по умолчению ставим 1 - первую страницу.
    page = paginator.get_page(page_number) # 128_Создаем обьект страници page с номером page_number

    is_paginated = page.has_other_pages() # 134_Переменная is_paginated может быть True или False - проверяет - есть ли еще страници
    if page.has_previous(): #135_Делаем проверку - Если есть предыдущие страници - тогда заполняется переменная prev_url
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if page.has_next(): #136_Делаем проверку - Если есть следующие страници - тогда заполняется переменная next_url
        next_url = f'?page={page.next_page_nember()}'
    else:
        next_url = ''

    context = {'page_object': page, # 137_Создаем словарь context для переменных
               'is_paginated': is_paginated, # Если нет страниц - чтоб не отображать кнопочки
               'prev_url': prev_url,
               'next_url': next_url
               }
    # return render(request, 'blog/index.html', context={'posts': posts})
    # return render(request, 'blog/index.html', context={'posts': page.object_list}) # 129_Заменяем в атрибуьте context значение posts на page.object_list
    return render(request, 'blog/index.html', context=context) # 131_Убираем свойство object_list - прописываем его в index.html
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
class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View): # 81_Создаем метод get класса TagCreate
    model_form = PostForm
    template = 'blog/post_create_form.html'
    raise_exeption=True # 123_Включаем метод  raise_exeption из класса LoginRequiredMixin - чтоб при попытке входа без права доступа выдавалась ошибка 403
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
class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View): # 92_Создаем class PostUpdate(ObjectUpdateMixin, View)
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exeption=True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View): # 100_Создаем class PostDelete(ObjectUpdateMixin, View) (blog/views.py)
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exeption=True

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

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View): #86_Переносим класс TagCreate из blog/views.py в blog/utils.py и делаем Миксин
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exeption=True
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

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View): #87 Создаем класс для изменения тэгов - class TagUpdate(View) - создаем методы get и post
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exeption=True
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
class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View): # 95_Создаем класс для удаления тегов, в нем реализуем два метода - get и post
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exeption=True
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
