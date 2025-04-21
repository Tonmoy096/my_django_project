from django.urls import path

'''from . import views
urlpatterns = [
    path('', views.hello_view),
]
'''
from .views import prodduct_list
urlpatterns = [
    path('', prodduct_list, name='home'),
    path('products/', prodduct_list, name='product_list'),
]