from django import forms
from .models import Category, Husband
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible



@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзиклмнопрстуфхцчшщьыъэюя0123456789-"
    code = 'russian'
    
    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис или пробел"

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': "form-input"}), validators=[RussianValidator(),])
    slug = forms.SlugField(max_length=255, label='URL', validators=[ MinLengthValidator(5), MaxLengthValidator(100)])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5}), required=False, label='Контент')
    is_published = forms.BooleanField(required=False, label='Публикация', initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории', empty_label='Не выбрано')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='Муж', empty_label='Не выбрано')