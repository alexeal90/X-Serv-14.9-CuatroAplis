#!/usr/bin/python


class holaApp():

    def parse(self, request, rest):
        palabra = request.split()[1][1:]
        return palabra

    def process(self, parsedRequest):
        htmlAnswer = ("<html><h2>" + str(parsedRequest) + "</h2></html>")
        return ("200 OK", htmlAnswer)

