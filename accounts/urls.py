from django.urls import path
from . import views # have to access view.py for http def's
urlpatterns = [
    path('',views.home , name="home"),
    path('products/',views.products , name='products'),
    path('customer/<str:pk_test>/',views.customer , name='customer')
]