
from .views import *
from django.urls import path

urlpatterns = [
    path('items/create/', ItemCreate.as_view(), name='item-create'), # POST request for retrieving item
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),  # GET request for retrieving item
    path('items/<int:pk>/update', ItemUpdate.as_view(), name='item-update'),  # PUT request for updating item
    path('items/<int:pk>/delete', ItemDelete.as_view(), name='item-delete'),  # DELETE request for deleting item
]
