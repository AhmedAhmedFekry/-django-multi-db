from django.urls import path
from home.api import views


urlpatterns = [


   
    ########################### products #########################
    path("product", views.products),
    path("product/create", views.createProduct),
    path("product/update/<int:id>", views.updateProduct),
    path("product/<int:id>", views.getProduct),
    path("product/delete/<int:id>", views.deleteProduct),
   


]