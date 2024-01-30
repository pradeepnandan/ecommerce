from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category,Products

# Create your views here.
# def index(request):
#     return render(request,'base.html')
    #return HttpResponse('Hello ')
def allProdCat(request,c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Products.objects.filter(category=c_page,available=True)
        return render(request, 'products.html', {'category': c_page, 'products': products})
    else:
        products=Products.objects.all().filter(available=True)
        return render(request,'category.html',{'category':c_page,'products':products})
def proDetails(request,c_slug,product_slug):
    try:
        product=Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product_det.html',{'product':product})
