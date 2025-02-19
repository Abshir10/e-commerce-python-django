


from . views import  home
from . import  views
from django.urls import  path

urlpatterns = [
    path('',home, name='home'),
    path('product/<int:id>/', views.productDetail, name='productDetail'),
]