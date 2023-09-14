from django.urls import path
from . import views # have to access view.py for http def's
urlpatterns = [
    path('',views.home ),
    path('products/',views.products),
    path('customer/',views.customer)
]