### here is the code needed to create a WSGI application interface to
### a Quixote app:

import quixote
import imageapp

imageapp.setup()
p = imageapp.create_publisher()
wsgi_app = quixote.get_wsgi_app()

def application(env,start_response):
	return wsgi_app(env,start_response)
