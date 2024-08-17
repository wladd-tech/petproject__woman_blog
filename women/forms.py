from django import forms
from .models import Category, Husband, Women
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


class AddPostForm(forms.ModelForm):
   
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории', empty_label='Не выбрано')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Муж', empty_label='Не выбрано')

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols':50, 'rows': 5}),
        }
        labels = {
            'slug': 'URL',
        }


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')