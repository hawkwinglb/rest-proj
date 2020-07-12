from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)

            context = {'order': order}
            return render(request, 'orders/order/created.html', context)
    else:
        form = OrderCreateForm()

    context = {'cart': cart, 'form': form}
    return render(request, 'orders/order/create.html', context)


def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders' : orders,
        }

    return render(request, 'orders/order/order_list.html', context)

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    context = {'order': order}

    return render(request, 'orders/order/order_detail.html', context)
