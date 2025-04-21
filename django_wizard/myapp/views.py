from django.shortcuts import render


'''def hello_view(request):
    context = {
        'name': 'Tonmoy The Wizard'
    }
    # render() tells django "find and load the home.html templates.
    return render(request, 'home.html', context)'''

from .models import Product

def prodduct_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
