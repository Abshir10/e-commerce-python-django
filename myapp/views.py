from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import  render
from .models import  products



def home(request) :
    myproducts = products.objects.all()
    # return HttpResponse("Welcome to My Django Project")
    return  render(request , 'home.html', {'products':myproducts})

def productDetail(request, id):
     product = get_object_or_404(products, product_id=id)
     # return render(request, 'productDetail.html', {'product': product})
     return render(request, 'productDetail.html', {'product': product})
