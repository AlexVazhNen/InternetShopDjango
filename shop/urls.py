from django.conf.urls import url
from . import views
from django.urls import path, include, re_path

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('<id>/<slug>', views.product_detail, name='product_detail'),
]
