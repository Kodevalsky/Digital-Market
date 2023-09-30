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

class ProductAddForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"tw-w-12 tw-rounded tw-border-gray-200 tw-py-3 tw-text-center tw-text-xs [-moz-appearance:_textfield] [&::-webkit-inner-spin-button]:tw-m-0 [&::-webkit-inner-spin-button]:tw-appearance-none [&::-webkit-outer-spin-button]:tw-m-0 [&::-webkit-outer-spin-button]:tw-appearance-none"}))
    size = forms.ChoiceField(choices=[("XS", 'S', 'M', 'L', 'XL')], widget=forms.RadioSelect(attrs={'class':""}))
    color = forms.ChoiceField(choices=[(1, "Texas Tea"), (2, "Fiesta Red"), (3,"Cobalt Blue")], widget=forms.RadioSelect(attrs={'class':"tw-peer tw-sr-only"}))