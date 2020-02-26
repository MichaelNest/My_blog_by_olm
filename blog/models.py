from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Post(models.Model): #16_ Создаем класс модели Post
    title = models.CharField(max_length = 150, db_index = True) # 17_Создаем поля для нашей модели Posts
    # max_length - это количества знаков этого поля, db_index=True - включенная автоматическая индексация поля
    slug = models.SlugField(max_length=150, unique=True) #18_Создаем параметр - удобночитаемый урл,
    # unique - параметр уникальности - автоматически индексируются
    # .SlugField() - позволяет использовать буквы в обоих регистрах, цифры, тире и нижнее подчеркивание
    body = models.TextField(blank=True, db_index=True) # 19_Создаем параметр для тела текста
    # blank=True - позволяет параметру body быть пустым
    data_pub = models.DateTimeField(auto_now_add=True) # 20_ Создаем параметр даты публикации
    # auto_now_add=True - будет сохранять дату публикации при каждом сохранении в базу данных
    # auto_now=True - будет сохранять дату публикации при каждом изменении поста

    def get_absolute_url(self): # 33_Будет возвращать ссылку на конкретный обьекм класса Post
        return reverse('post_detail_url', kwargs={'slug': self.slug})


    def __str__(self):
        return f'{self.title}' # этот метод отвечает за вывод информации об обьекте. Будем выдавать содержимое поля title

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
