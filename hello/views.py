from django.shortcuts import render
from django.http import HttpResponse

from mcstatus import MinecraftServer

from .models import Greeting

import json

# Create your views here.
def index(request):		
	# Get the server
	server = MinecraftServer.lookup("www.yourServerHere.com:25565")

	# Get the status and query data, requires two calls to get everything.
	status = server.status()
	query = server.query()

	# Create the object to store all the server data.
	req = {}
		
	req['playerCount'] = status.players.online
	req['maxPlayers'] = status.players.max

	req['playerNames'] = query.players.names
	
	req['version'] = query.software.version;
	req['motd'] = query.motd;
	req['map'] = query.map;

	# Package the requested data into the callback for JSONP
	callback = request.GET.get('callback', '')
	response = json.dumps(req)
	response = callback + '(' + response + ');'

	return HttpResponse(response, content_type="application/json")
		
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

