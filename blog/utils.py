from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.shortcuts import get_object_or_404
# 58_Создаем файл utils.py, чтоб устранить избыточный код во views.py

class ObjectDetailMixin: # 59_Создаем свой класс, определяем переменные для модели и шаблона (model, template)
    model=None
    template=None
    def get(self, request, slug): #60_ копируем метод get и изменяем его переменные
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_object': obj, 'detail': True})
        # 111_Добавляем в class ObjectDetailMixin в context еще один атрибут - 'admin_object': obj
        # 113_Добавляем в class ObjectDetailMixin в context еще один атрибут - 'detail': True
class ObjectCreateMixin: #86_Переносим класс TagCreate из blog/views.py в blog/utils.py и делаем Миксин - class ObjectCreateMixin
    model_form = None
    template = None
    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj= bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})

class ObjectUpdateMixin: #91 Создаем Mixin-класс для изменения тэгов - class ObjectUpdateMixin
    model = None
    model_form = None
    template = None
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form':bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj= self.model.objects.get(slug__iexist=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid:
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form':bound_form, self.model.__name__.lover(): obj})

class ObjectDeleteMixin: #99 Создаем Mixin-класс для изменения тэгов - class ObjectDeleteMixin
    model = None
    template = None
    redirect_url = None
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower():obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url)
