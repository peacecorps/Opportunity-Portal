from google.appengine.ext import db

class Opportunity(db.Model):
    title = db.StringProperty()#Column B of the JSR Full extract
    description = db.TextProperty() #Corresponds to the description of the project. Column C of the JSR full extract
    position_remaining = db.IntegerProperty(default=0) #number of positions remaining for a specific opportunity. Column E of the JSR full extract
    region = db.StringProperty() #Corresponds to the sub-region part of the excel file. Column G of the JSR full extract
    start_date = db.DateTimeProperty()
    apply_date = db.DateTimeProperty
    sector = db.StringProperty()