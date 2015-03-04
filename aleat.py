#!/usr/bin/python

"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

	Alejandro Valeriano Fernandez - GITT
	Ejercicio 14.2
	Server
"""

import random
import webapp

class randomApp ():

    def parse(self, request, rest):
        return "Listo"

    def process(self, parsedRequest):
        randNum = str (random.randint (0,10000))
        randomURL = ("<html><a href= /aleat>Dame otra</a></html>" + str(randNum))
        return ("200 OK", randomURL)

