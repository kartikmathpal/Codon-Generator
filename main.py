#!/usr/bin/env python

import os
import urllib

import cgi

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello world!')

class Processor(webapp2.RequestHandler):
    def post(self):
        input = self.request.get('input')
        output = ""

        # Remove all carriage returns from the sequence
        sequence = input.replace(" ", "").replace("\n", "").replace("\r", "")

        ######################################################################
        ##### PRINT OUT *SEQUENCE* THREE NUCLEOTIDES AT A TIME ###############
        ######################################################################

        # Assuming we have a coding sequence, print out each codon
        startOfCodon = 0
        while (startOfCodon < len(sequence)):
            codon = sequence[startOfCodon:startOfCodon+3]
            output += codon + "\n"
            startOfCodon = startOfCodon + 3

        template_values = {
            'input': input,
            'output': output
        }

        template = JINJA_ENVIRONMENT.get_template('templates/output.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/api/', MainHandler),
    ('/api/process', Processor)
], debug=True)
