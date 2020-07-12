from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView
from django.db.models import Q

from .models import Category, Product
from cart.forms import CartAddProductForm
from orders.models import Order, OrderItem

class SearchProductsView(ListView):
    model = Product
    template_name = "foodshop/product/search_view.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(Q(name__icontains=query) | Q(allergens__icontains=query))
        return object_list


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        }
    return render(request, 'foodshop/product/product_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product,
               'cart_product_form': cart_product_form}
    return render(request, 'foodshop/product/product_detail.html', context)




