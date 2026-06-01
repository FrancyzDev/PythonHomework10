from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()

    products_list = Product.objects.all()

    context = {
        'title': 'Продукти',
        'products': products_list,
        'form': form
    }
    return render(request, 'products.html', context)
