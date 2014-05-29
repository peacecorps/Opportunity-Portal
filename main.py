#!/usr/bin/env python
#
#  Opportunity Portal
# 
#  https://github.com/PeaceCorps/Opportunity-Portal
#
#
#  For Questions email:ktu219@gmail.com
#

import os
import webapp2
from google.appengine.ext.webapp import template

class BaseHandler(webapp2.RequestHandler):
    def render_template(self, file, template_args):
        path = os.path.join(os.path.dirname(__file__), file)
        self.response.out.write(template.render(path, template_args))

# Index
# -------------------
# We shouldd maintain the same file explore.html instead of copy and replace the old index.html
class indexHandler(BaseHandler):
    def get(self):
        self.render_template("explore.html", dict())

# Opportunity Handler
# -------------------
# This should display different opportunity base on the request get from filter page
# Use /opportunity instead of /opportunity/ is easier to develop without set up the GAE environment.
class opportunityHandler(BaseHandler):
    def get(self):
        self.render_template("opportunity.html", dict())

# Static File Handler
# -------------------
# This should be temporary handler for static files
# eventually we should decide which pages we are going to keep in our opt-finder
class staticFileHandler(BaseHandler):
    def get(self, filename):
        # Temporary host static filelist in this way
        filelist = ["apply.html","about.html","contact.html","explore.html"]
        if filename not in filelist:
            self.error(404)
            # Borrow 404 from github
            self.render_template("404.html", dict())
            return
        self.render_template(filename, dict())

app = webapp2.WSGIApplication([
    ('/', indexHandler),
    ('/index.html', indexHandler),
    ('/opportunity', opportunityHandler),
    ('/([^/]+)?', staticFileHandler)
], debug=True)
