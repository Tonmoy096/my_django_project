from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})



'''from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm  # Assuming you have a form for Product

# List all products
def product_list(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'product_list.html', {'products': products})

# Create a new product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)  # Use the ProductForm to handle form submission
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm()  # Empty form if GET request
    return render(request, 'product_create.html', {'form': form})'''