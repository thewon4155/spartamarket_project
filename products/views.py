from django.shortcuts import render

def product_list(request):
    return render(request, 'products/product_list.html')

def product_detail(request):
    return render(request, 'products/product_detail.html')

def product_create(request):
    return render(request, 'products/product_create.html')

def product_update(request):
    return render(request, 'products/product_update.html')

def product_delete(request):
    return render(request, 'products/product_delete.html')
