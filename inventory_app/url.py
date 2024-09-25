from django.urls import path
from .views import ItemDetail

urlpatterns = [
    path('inventory/items/',ItemDetail.as_view()),
    path('inventory/items/<int:id_id>',ItemDetail.as_view()),
]
