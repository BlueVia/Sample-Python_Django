from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from purchases.models import Purchase
from purchases.models import Product

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'purchases.views.home', name='home'),
    url(r'^movies$', 'purchases.views.movies', name='movies'),
    url(r'^purchase/(?P<product_id>\w+)', 'purchases.views.purchase', name='purchase'),
    url(r'^authorized/(?P<product_id>\w+)', 'purchases.views.authorized', name='authorized'),

    # url(r'^bvstore/', include('bvstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^purchaselist$',
        ListView.as_view(
            queryset=Purchase.objects.all(),
            context_object_name='purchase_list',
            template_name='purchase_list.html'),name='purchaselist'),

    url(r'^productlist$',
        ListView.as_view(
            queryset=Product.objects.all(),
            context_object_name='product_list',
            template_name='product_list.html'),name='productlist'),
)
