from django import forms
from django.forms import BooleanField

from catalog.models import Product, Category, Version


class StileFormMixin:
    """Class Mixin for stilization forms"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StileFormMixin, forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data.get('name')
        print(name)
        exceptions = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                      'радар']

        for word in name.split(' '):
            if word.lower() in exceptions:
                raise forms.ValidationError(f"Нельзя использовать слово {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        exceptions = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                      'радар']

        for word in description.split(' '):
            if word.lower() in exceptions:
                raise forms.ValidationError(f"Нельзя использовать слово {word}")
        return description

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at",)


class CategoryForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class VersionForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
