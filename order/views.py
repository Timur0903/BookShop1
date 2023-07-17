from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateOrderForm
from .models import Order

# Create your views here.

def create_order(requset):
    print(requset.POST)
    order_form = CreateOrderForm(requset.POST)
    if order_form.is_valid():
        print(order_form.cleaned_data)
        # order = Order.objects.create(**order_form.cleaned_data)
        order_form.save()
        return render(requset, 'order/order.html', {'form': order_form})
    order_form = CreateOrderForm()
    return render(requset, 'order/order.html', {'form': order_form})

