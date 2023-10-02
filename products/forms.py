from django import forms 
from .models import Product, CartItem

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

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ("owner", "item", "quantity", "attribute1", "attribute2")
    quantity = forms.IntegerField(\
        widget=forms.NumberInput(\
            attrs={'class':"tw-w-12 tw-rounded tw-border-gray-200 tw-py-3 tw-text-center tw-text-xs [-moz-appearance:_textfield] [&::-webkit-inner-spin-button]:tw-m-0 [&::-webkit-inner-spin-button]:tw-appearance-none [&::-webkit-outer-spin-button]:tw-m-0 [&::-webkit-outer-spin-button]:tw-appearance-none"}))
    attribute1 = forms.ChoiceField(\
        choices=[(1, "Texas Tea"), (2, "Fiesta Red"), (3,"Cobalt Blue")], \
            widget=forms.RadioSelect(\
                attrs={'class':"tw-peer tw-sr-only"}),\
                     label="Size")
    attribute2 = forms.ChoiceField(\
        choices=[(1, "XS"), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')], \
            widget=forms.RadioSelect(\
                attrs={'class':"tw-peer tw-sr-only"}),\
                    label="Color")