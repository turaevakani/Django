from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import OrderForm
from .models import ProductCL, TagCL, OrderCL, CustomerCL
from django.views.generic import ListView
from django.views import generic

class ProductListView(generic.ListView):

    queryset = ProductCL.objects.filter().order_by('-id')  # for filter order_by('-id')
    template_name = 'cloth/product_list.html'

    def get_queryset(self):
        return self.queryset

def products_by_tag(request, tag_name):
    tag = get_object_or_404(TagCL, name=tag_name)
    products = ProductCL.objects.filter(tag=tag)
    context = {'products': products, 'tag': tag}
    return render(request, 'cloth/product_by_tag.html', context)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data.get('customer_name')
            customer, created = CustomerCL.objects.get_or_create(name=customer_name)

            order = form.save(commit=False)
            order.customer = customer

            order.save()
            form.save_m2m()
            # order = form.save(commit=False)
            # order.customer = request.customer
            # order.save()
            # form.save_m2m()

            return HttpResponse('<h1>The comment was successfully added!</h1>')
    else:
        form = OrderForm()

    return render(request, 'cloth/create_order.html', {'form': form})

# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#
#             order.save()
#             return render(request, 'cloth/order_created.html', {'order': order})
#     else:
#         form = OrderForm()
#     return render(request, 'cloth/create_order.html', {'form': form})

def men_clothing(request):
    return products_by_tag(request, 'men')

def women_clothing(request):
    return products_by_tag(request, 'women')

def kids_clothing(request):
    return products_by_tag(request, 'kids')

def unisex_clothing(request):
    return products_by_tag(request, 'unisex')
