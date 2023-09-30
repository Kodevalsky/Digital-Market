from django.shortcuts import render

from .forms import ProductForm, RawProductForm, ProductAddForm

from .models import Product, Cart

# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == "GET":
        product_list = Product.objects.all()
        form = ProductAddForm()
        context = {"obj": product_list, "form": form}
        return render(request, "products/home.html", context)
    if request.method == "POST":
        #AddedProduct = Cart(owner= , item= , quantity = )
        pass

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