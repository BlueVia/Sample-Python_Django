Sample-Python_Django
====================

Demo of Bluevia Payment API in a Python/Django application

To deploy it locally just:

- Clone this repository locally
- Create a virtual environment
- Install the requirements (pip install -r requitements.txt). psycopg2 and dj-database-url are not required to deploy locally
- Execute Django syncdb
- Provision the products with the script bvstore/purchases/provisioning.py script
- Provision the BVApp with your payment API Key consumer key and secret
- Start your django server
- Enjoy!

You can see it working here:
- Heroku: http://circusapp.herokuapp.com/
- Instant Servers: http://81.45.18.53:8000

More info:
http://www.slideshare.net/bluevia/aprende-a-crear-y-desplegar-una-aplicacin-de-python-que-use-apis-de-bluevia