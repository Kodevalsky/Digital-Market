from django.shortcuts import render

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.
def home_view(request, *args, **kwargs):
    product_list = Product.objects.all()
    context = {"obj": product_list}
    return render(request, "products/home.html", context)

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text":"This is about us",
        "my_number": 123,
        "my_list":[1,2,3,4]
    }
    return render(request, "products/about.html", my_context)

def product_detail_view(request):
    obj = Product.objects.geT(id=1)
    return render(request, "product/detail.html")

def cart_page(request):
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

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

def ProductCreateView(request):
    my_form = RawProductForm()
    context = {'form': my_form}
    return render(request, "products/product_create.html", context)