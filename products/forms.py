from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image','price', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введіть назву товару'
            }),
            'image': forms.ClearableFileInput(attrs={
                'placeholder': 'Виберіть зображення товару'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Введіть ціну (наприклад: 99.99)',
                'step': '0.01'
            }),
            'calories': forms.NumberInput(attrs={
                'placeholder': 'Введіть калорійність (наприклад: 250)'
            })
        }
        labels = {
            'name': 'Назва товару',
            'image': 'Зображення товару',
            'price': 'Цiна',
            'calories': 'Калорiйнiсть',
        }