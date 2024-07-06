from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', ' дешево', 'бесплатно', 'обман', 'полиция',
                        'радар']
        for banned_word in banned_words:
            if banned_word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать слово "{banned_word}" для названия товара')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', ' дешево', 'бесплатно', 'обман', 'полиция',
                        'радар']
        for banned_word in banned_words:
            if banned_word in cleaned_data.lower():
                raise forms.ValidationError(f'Нельзя использовать слово "{banned_word}" для описания товара')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
