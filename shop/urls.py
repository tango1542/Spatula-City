from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),                #This URL pattern is for all products
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),      #This URL pattern is for if a category is selected
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),       #This URL pattern is for the details view..via product id
]