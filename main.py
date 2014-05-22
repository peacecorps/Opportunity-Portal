#!/usr/bin/env python
#
# 
#  ktu219@gmail.com

import os
import webapp2
from google.appengine.ext.webapp import template

class BaseHandler(webapp2.RequestHandler):
    def render_template(self, file, template_args):
        path = os.path.join(os.path.dirname(__file__), file)
        self.response.out.write(template.render(path, template_args))

# index.html
class indexHandler(BaseHandler):
    def get(self):
        self.render_template("index.html", dict())

# For general static files
class staticFileHandler(BaseHandler):
    def get(self, filename):
        self.render_template(filename, dict())

app = webapp2.WSGIApplication([
    ('/', indexHandler),
    ('/([^/]+)?', staticFileHandler)
], debug=True)
