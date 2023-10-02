from django.shortcuts import render, get_object_or_404

from .forms import RawProductForm, ProductAddForm

from .models import Product, Cart

from django.contrib.auth.decorators import login_required

# Create your views here.

def BrowseView(request, *args, **kwargs):
    if request.method == "GET":
        product_list = Product.objects.all()
        form = ProductAddForm(auto_id='test_%s')
        context = {"obj": product_list, "form": form}
        return render(request, "products/browse.html", context)
    if request.method == "POST":
        #AddedProduct = Cart(owner= , item= , quantity = )
        pass

@login_required
def CartPage(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form':form
    }
    return render(request, 'products/cartwebpage.html', context)

def ProductView(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'obj' : product}
    return render(request, 'products/productview.html', context)