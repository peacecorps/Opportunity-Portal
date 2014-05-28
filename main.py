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
        self.render_template("view/index.html", dict())

class opportunityHandler(BaseHandler):
    def get(self, opportunityCode):
    	if opportunityCode == None:
    		opportunityCode = "Insert code here"
    	args = dict(
    		opportunityCode = opportunityCode
    		)
        self.render_template("view/opportunity.html", args)

app = webapp2.WSGIApplication([
    ('/', indexHandler),
    ('/opportunity/([^/]+)?', opportunityHandler),
], debug=True)
