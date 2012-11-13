from django.db import models
from django.contrib import admin

class BVApp(models.Model):
    consumer_key = models.CharField(max_length=40)
    consumer_secret = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    app_id = models.CharField(max_length=40)
    mo_keyword = models.CharField(max_length=15)
    
    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40)
    content_url = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    price = models.IntegerField()
    currency = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name + "-" + str(self.price) + " " + self.currency

class Purchase(models.Model):
    app = models.ForeignKey(BVApp)
    #product_name = models.CharField(max_length=15)
    product = models.ForeignKey(Product)
    msisdn = models.CharField(max_length=15)
    purchase_date = models.DateTimeField('date purchased')

    def __unicode__(self):
        return self.msisdn + "-" + self.product_name


admin.site.register(BVApp)
admin.site.register(Purchase)
admin.site.register(Product)