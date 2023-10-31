from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductAddForm

from .models import Product, CartItem

from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

# Create your views here.


from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductAddForm
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required

class SearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(title__icontains=query)
        else:
            products = Product.objects.all()
        context = {'obj': products}
        return render(request, 'products/browse.html', context)


class BrowseView(View):
    def get(self, request):
        product_list = Product.objects.all()
        form = ProductAddForm()
        context = {"obj": product_list, "form": form}
        return render(request, "products/browse.html", context)
    
    def post(self, request):
        form = ProductAddForm(request.POST)
        if form.is_valid():
            product_id = request.POST.get('product_id')
            quantity = form.cleaned_data['quantity']
            attribute1 = form.cleaned_data['attribute1']
            attribute2 = form.cleaned_data['attribute2']
            owner = request.user

            # Check if a CartItem object with the same product and owner already exists
            cart_item = CartItem.objects.filter(item_id=product_id, owner=owner).first()

            if cart_item:
                # If a CartItem object already exists, update the quantity
                cart_item.quantity += quantity
                cart_item.save()
            else:
                # If a CartItem object doesn't exist, create a new one
                item = form.save(commit=False)
                item.owner = owner
                item.item = get_object_or_404(Product, id=product_id)
                item.save()

            # Redirect to the cart page
            return redirect('cart')

        # Handle form validation errors here
        product_list = Product.objects.all()
        context = {"obj": product_list, "form": form}
        return render(request, "products/browse.html", context)

@login_required
def CartPage(request):
    if request.method == "GET":
        UserCart = CartItem.objects.filter(owner=request.user)
        price = 0
        for item in UserCart:
            price += item.quantity * item.item.price
        context = {'UserCart': UserCart, 'total':price}
        return render(request, 'products/cartwebpage.html', context)


def ProductView(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'obj' : product}
    return render(request, 'products/productview.html', context)


@login_required
def ProductDeleteView(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
    UserCart = CartItem.objects.filter(owner=request.user)
    price = 0
    for item in UserCart:
        price += item.quantity * item.item.price
    context = {'UserCart': UserCart, 'total':price}
    return render(request, 'products/cartwebpage.html', context)