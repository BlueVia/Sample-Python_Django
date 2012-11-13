from purchases.models import Product

p = Product(name='SkyFall',content_url='http://www.youtube.com/embed/6kw1UVovByw',image_url='http://81.45.18.53:8000/static/images/skyfall.jpg',price='2',currency='GBP')
p.save()

p = Product(name='GoldenEye',content_url='http://www.youtube.com/embed/TUNP9xrOBd4',image_url='http://81.45.18.53:8000/static/images/goldeneye.jpg',price='2',currency='GBP')
p.save()

p = Product(name='GoldFinger',content_url='http://www.youtube.com/embed/KdQoSK9wibU',image_url='http://81.45.18.53:8000/static/images/goldfinger.jpg',price='2',currency='GBP')
p.save()

p = Product(name='Quantum of Solace',content_url='http://www.youtube.com/embed/KdQoSK9wibU',image_url='http://81.45.18.53:8000/static/images/quantum.jpg',price='2',currency='GBP')
p.save()

p = Product(name='Agente 007 contra el doctor No',content_url='http://www.youtube.com/embed/KdQoSK9wibU',image_url='http://81.45.18.53:8000/static/images/drno.jpg',price='2',currency='GBP')
p.save()

p = Product(name='Desde Rusia con Amor',content_url='http://www.youtube.com/embed/KdQoSK9wibU',image_url='http://81.45.18.53:8000/static/images/russia.jpg',price='2',currency='GBP')
p.save()