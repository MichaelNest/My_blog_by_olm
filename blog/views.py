from django.shortcuts import render

# Create your views here.
def posts_list(request):
    names = ['Misha', 'Pasha', 'Sasha', 'Dasha']
    return render(request, 'blog/index.html', context={'names': names})
    #5_ Возвращаем на исполнение метод render и указываем на наш шаблон index.html
    #6_ Вводим переменную context, в которой можем вносить данные в виде словаря
