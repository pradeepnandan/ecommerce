from .models import Cartitem,Cart
from .views import _cart_id
def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            car_items=Cartitem.objects.all().filter(cart=cart[:1])
            for car_item in car_items:
                item_count+=car_item.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)