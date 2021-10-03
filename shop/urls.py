from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('(?P<id>\d+)/(?P<slug>[-\w]+)/', views.product_detail, name='product_detail'),
]
#
#
# urlpatterns = [
#     path('index/', views.index, name='main-view'),
#     path('bio/<username>/', views.bio, name='bio'),
#     path('articles/<slug:title>/', views.article, name='article-detail'),
#     path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
#     path('weblog/', include('blog.urls')),
#     ...
# ]