# encoding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from datetime import datetime
import oauth2 as oauth
import bluevia

from purchases.models import BVApp
from purchases.models import Purchase
from purchases.models import Product

def home(request):
    #return HttpResponse("Hola mundo. Estás en la home.")
    return redirect('movies')

def movies(request):
    # return HttpResponse("Hola mundo. Estás en la categoría de películas.")
    return render_to_response('store.html',
                               context_instance=RequestContext(request))
def purchase(request,product_id):
    apps = BVApp.objects.all()
    bvapp = apps[0]

    bvpayment = bluevia.BlueViaPayment(bvapp.consumer_key, bvapp.consumer_secret,sandbox='')
    bvpayment.setDebug(True)

    # ES
    #price=182
    #currency='EUR'
    # UK
    price=200
    currency='GBP'
    # DE
    #price=99
    #currency='EUR'

    url = request.build_absolute_uri(reverse('authorized', args=[product_id]))
    result = bvpayment.fetch_request_token(price,currency,
        '963dd2a0601e8f7de6d22f46',
        'Bluevia Movies Store',
                            callback=url) #<amount>, <currency>, <serviceId>, <serviceName>
    
    request.session['payment_info'] = bvpayment.getPaymentInfo()
    request.session['request_token'] = bvpayment.request_token

    return redirect(result[1])
    #return HttpResponse('Comprando')

def authorized(request,product_id):
    if request.GET:
        bvapp = BVApp.objects.all()[0]

        bvpayment = bluevia.BlueViaPayment(bvapp.consumer_key, bvapp.consumer_secret)
        bvpayment.initPaymentInfo(str(request.session['payment_info']))
        bvpayment.request_token = oauth.Token.from_string(str(request.session['request_token']))

        verifier = request.GET['oauth_verifier']
        bvpayment.fetch_access_token(str(verifier))  # A bug in the library??
        bvpayment.issuePayment()
        #bvpayment.checkPayment(<transactionId>)

        p = Product.objects.get(pk=product_id)

        purchase = Purchase(app=bvapp, product=p, msisdn="447548316219", purchase_date=datetime.now())
        purchase.save()

    return redirect('movies')
