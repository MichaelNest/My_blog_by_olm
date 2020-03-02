# 63_Создаем новый файл - forms.py
from django import forms
from .models import Tag
from django.core.exeptions import ValidationError

class TagForm(forms.ModelForm): #64_Создаем класс модели для форм
# 76_Модернизируем наш класс TagForm , наследуя его от класса МodelForm и введя class Meta
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class': 'form-control'}) # 73_Прописываем для наших полей ввода стилистику Bootstrap
    # slug.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Tag
        fields =['title', 'slug']
        widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
                   'slug': forms.TextInput(attrs={'class': 'form-control'})}


    def clean_slug(self): # 66_Создаем метод для приведения поля slug к нижнему регистру
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create': # 67_Создаем условие проверки на недопустимые нами слова для тегов
            raise ValidationError('Slug may not be "Create".')
        if Tag.objects.filter(slug__iexact=new_slug).count(): # 75_ Делаем проверку на повторяющееся название slug
            raise ValidationError(f'Slug mast be unique. We have {new_slug} slug already')
        return new_slug

    # def save(self): # 65_Переопределяем метод сохранения обьекта
    #     new_tag = Tag.objects.create(title = self.cleaned_data['title'], slug = self.cleaned_data['slug'])
    #     return new_tag
    # 77_Убираем метод save(self), потому что метод ModelForm имеет встроеный метод save
