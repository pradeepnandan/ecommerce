from django.shortcuts import render, redirect, get_object_or_404
from ecommerceapp.models import Products
from .models import Cart, Cartitem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def add_cart(request,product_id):
    product=Products.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item=Cartitem.objects.get(product=product,cart=cart)
        cart_item.quantity+=1
        cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item=Cartitem.objects.create(product=product,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cart_app:cart_details')
def cart_details (request, total=0,counter=0,cart_item=None):
    cat_price_dic={}
    list1=[]
    cat_qty=0
    price=0
    tot_cat_price=0
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=Cartitem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter+=cart_item.quantity
            if cart_item.product.category.name in cat_price_dic:
                #price1=cat_price_dic.get(cart_item.product.category.name)
                price=cart_item.product.price*cart_item.quantity
                print('price of veg',cart_item.product.price,cat_price_dic)
                tot_cat_price=price + cat_price_dic.get(cart_item.product.category.name)

                cat_price_dic.update({cart_item.product.category.name:tot_cat_price})
                print('inside if...', price, cart_item.quantity, cat_price_dic, cart_item.product.category.name)
            else:
                price1=cart_item.product.price*cart_item.quantity
                cat_price_dic.update({cart_item.product.category.name:price1 })
                print('inside else...',price1,cart_item.quantity,cat_price_dic,cart_item.product.category.name)
        print(cat_price_dic)
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter,cat_price_dic=cat_price_dic))

def remove_cart(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Products,id=product_id)
    cart_item=Cartitem.objects.get(product=product,cart=cart)
    if cart_item.quantity>1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_details')
