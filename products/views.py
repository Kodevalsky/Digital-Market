from django.shortcuts import render, get_object_or_404

from .forms import RawProductForm, ProductAddForm

from .models import Product, CartItem

from django.contrib.auth.decorators import login_required

# Create your views here.

def BrowseView(request, *args, **kwargs):
    if request.method == "GET":
        product_list = Product.objects.all()
        form = ProductAddForm(auto_id='test_%s')
        context = {"obj": product_list, "form": form}
        return render(request, "products/browse.html", context)
    
    if request.method == "POST":
        form = ProductAddForm(request.POST)
        if form.is_valid():
            print('penis')
            item = form.save(commit=False)  # Create a CartItem instance but don't save it yet
            item.owner = request.user
            item.item = get_object_or_404(Product, id=request.POST.get('product_id'))  # Adjust this line if needed
            item.save()  # Save the CartItem instance to the database
            
            # Redirect to a success page or update the context as needed
            return redirect('products/browse.html')  # Replace 'success_page' with the actual URL name

        # Handle form validation errors here
        context = {"obj": Product.objects.all(), "form": form}
        return render(request, "products/browse.html", context)

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