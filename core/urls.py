from django.urls import path
from .views import (
    # item_list,
    ItemDetailview,
    checkout,
    HomeView
)

app_name = 'core'

urlpatterns = [
    # path('', item_list, name='item_list'),
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ItemDetailview.as_view(), name='product')
]