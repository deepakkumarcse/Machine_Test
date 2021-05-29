from django import forms
from .models import Category, Tag, Product


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'nameId'}),
        }


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'nameId'}),
        }


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'nameId'}),
        }
