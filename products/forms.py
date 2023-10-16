from django import forms 
from .models import Product, CartItem

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ("quantity", "attribute1", "attribute2")
    quantity = forms.IntegerField(\
        widget=forms.NumberInput(\
            attrs={'min':"1", 'value':"1", 'class':"tw-border-gray-900 tw-border-2 tw-w-12 tw-rounded tw-border-gray-200 tw-py-3 tw-text-center tw-text-xs [-moz-appearance:_textfield] [&::-webkit-inner-spin-button]:tw-m-0 [&::-webkit-inner-spin-button]:tw-appearance-none [&::-webkit-outer-spin-button]:tw-m-0 [&::-webkit-outer-spin-button]:tw-appearance-none"}))
    attribute1 = forms.ChoiceField(\
        choices=[('TT', "Texas Tea"), ('FR', "Fiesta Red"), ('CB',"Cobalt Blue")], \
            widget=forms.RadioSelect(\
                attrs={'class':"tw-peer tw-sr-only"}),\
                     label="Size")
    attribute2 = forms.ChoiceField(\
        choices=[('XS', "XS"), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], \
            widget=forms.RadioSelect(\
                attrs={'class':"tw-peer tw-sr-only"}),\
                    label="Color")