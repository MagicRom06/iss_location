#coding:UTF-8

import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/astros.json'
reponse = urllib.request.urlopen(url)
result = json.loads(reponse.read())

print('Personne actuellement dans l\'espace: {}'.format(result['number']))

people = result['people']

for elt in people:
	print('{} dans {}'.format(elt['name'], elt['craft']))

url = 'http://api.open-notify.org/iss-now.json'
reponse = urllib.request.urlopen(url)
result = json.loads(reponse.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])

print('Latitude {}'.format(lat))
print('Longitude {}'.format(lon))

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

time.sleep(20)
