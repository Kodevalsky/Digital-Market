from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label='title')
    description = forms.CharField(required = False, \
        widget=forms.Textarea())
    price = forms.DecimalField(required=True, \
        widget=forms.NumberInput(\
            attrs={"id": "quantityinput",\
                "class": "h-8 w-8 border bg-white text-center text-xs outline-none",\
                "value": "2",\
                "min": "1"}))