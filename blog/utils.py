from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# 58_Создаем файл utils.py, чтоб устранить избыточный код во views.py

class ObjectDetailMixin: # 59_Создаем свой класс, определяем переменные для модели и шаблона (model, template)
    model=None
    template=None
    def get(self, request, slug): #60_ копируем метод get и изменяем его переменные
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
