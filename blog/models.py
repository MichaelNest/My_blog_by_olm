from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(s): # 83_Создаем метод для автоматической генерации slug - def gen_slug(s)
    new_slug = slugify(s, allow_unicode=True) # 84_Используем метод slugify - он автоматически из имени title делает slug
    return new_slug +'-'+str(int(time()))
# >>> allow_unicode = True - нужно включить, чтоб метод slugify понимал киррилицу
# >>> time() - генерирует количество секунд с 1970 года да настоящего момента. Используем это как уникальный идентификатор
# Create your models here.
class Post(models.Model): #16_ Создаем класс модели Post
    title = models.CharField(max_length = 150, db_index = True) # 17_Создаем поля для нашей модели Posts
    # max_length - это количества знаков этого поля, db_index=True - включенная автоматическая индексация поля
    slug = models.SlugField(max_length=150, blank=True, unique=True) #18_Создаем параметр - удобночитаемый урл,
    # unique - параметр уникальности - автоматически индексируются
    # .SlugField() - позволяет использовать буквы в обоих регистрах, цифры, тире и нижнее подчеркивание
    body = models.TextField(blank=True, db_index=True) # 19_Создаем параметр для тела текста
    # blank=True - позволяет параметру body быть пустым
    data_pub = models.DateTimeField(auto_now_add=True) # 20_ Создаем параметр даты публикации
    # auto_now_add=True - будет сохранять дату публикации при каждом сохранении в базу данных
    # auto_now=True - будет сохранять дату публикации при каждом изменении поста
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    # 36_Создаем параметр, связывающий два класса Post и Tag. blank=True - дозволяет посту не иметь тега.
    # Если параметр tags в посте указывает на все привязанные к этому посту тэги,
    # То параметром related_name='posts' мы задаем свойство posts - которое появится у экземпляров tag

    def get_absolute_url(self): # 33_Будет возвращать ссылку на конкретный обьекм класса Post
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self): # 90_Создаем метод для ссылки на конкретный обьект
        return reverse('post_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self): #98_ Создаем метод get_delete_url(self) для ссылки на конкретный обьект
        return reverse('post_delete_url', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs): # 85_Переопределяем метод save класса Post - для того чтоб генерировать новый slug только при создании экземпляра класса Post.
        if not self.id:
            self.slug = gen_slug(self.title)
            super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.title}' # этот метод отвечает за вывод информации об обьекте. Будем выдавать содержимое поля title

class Tag(models.Model): # 35_Создаем модель Tag для тэгов
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})
    # 49_Создаем в моделях метод для ссылки на конкретный обьект класса Tag

    def get_update_url(self): # 90_Создаем метод get_update_url(self) для ссылки на конкретный обьект
        return reverse('tag_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self): #98_ Создаем метод get_delete_url(self) для ссылки на конкретный обьект
        return reverse('tag_delete_url', kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.title}'
    # 21_ Создаем миграции - переносим нашу модель Post в базу данных (находясь в виртуальном окружении):
    # python manage.py makemigrations
    # python manage.py migrate
    # 22_ Заходим в консоль Django чтоб через нее создавать обьекты модели Post в базе данных - создавать посты и управлять ими
    # python managt.py shell -  команда захода в консоль

    # >>> from blog.models import Post
    # >>> p = Post(title='New Post_1', slug='new_post_1', body='New Post_1 Body Text') - создаем обьект
    # >>> p.save() - сохраняем обьект
    # >>> p.id - посмотреть id обьекта, который появится после сохранения его в базе данных
    # >>> dir(p) - посмотреть все атрибуты нашего обьекта p
    # >>> p1 = Post.objects.create(title='New Post_1_0', slug='new_post_1_0', body='New Post_1_0 Body Text') - создаем обьект через менеджер-команду objects
    # >>> Post.objects.all() - посмотреть все имеющиеся обьекты
    # >>> post = Post.objects.get(slug='new_post_1') - в post возвращается тот наш обьект, у которого будет указанный slug
    # >>> post = Post.objects.get(slug__iexact='new_post_1') - примененин lookups - параметры для управлением кретериями поиска
    # >>> __iexact - это lookup - i - значит регистронезависимый, exact - значит полное совпадение
    # >>> .get - возвращаем один обьект. .filter - может возвращать несколько обьектов
    # >>> post = Post.objects.filter(slug__contains='new') - выдаст все обьекты с 'new' в значении slug
    # >>> __contains - это lookup - значит выдать все обьекты, где в значении slug есть слово 'new'

    # 37 Заходим в консоль Django чтоб через нее создавать обьекты модели Tag в базе данных - создавать посты и управлять ими
    # python managt.py shell -  команда захода в консоль

    # >>> from blog.models import *
    # >>> django_t = Tag.objects.create(title='django', slug='django') - создаем обьект тэга
    # >>> Post.objects.values() - отобразит все наши обьекты-посты и их свойства и методы
    # >>> post = Post.objects.get(slug='new_slug_1')
    # >>> post.slug = 'new_post_1'
    # >>> post.save()
    # >>> post.tags.add(django_t) - добавили обьекту post обьект django_t через менеджер tag - т е мы связали пост и тег
    # >>> post.tags.all() - посмотеть все тэги прикрепленные к посту post.
    # >>> django_t.posts.all() - покажет все посты, прикрепленные к этому обьекту тэга.
    # >>>
