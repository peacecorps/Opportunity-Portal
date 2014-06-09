from django.db import models


class Opportunity(models.Model):
    title = models.CharField(max_length=200) #Column B of the JSR Full extract
    description=models.CharField(max_length=2000) #Corresponds to the description of the project. Column C of the JSR full extract
    position_remaining=models.IntegerField(default=0) #number of positions remaining for a specific opportunity. Column E of the JSR full extract
    region=models.CharField(max_length=200) #Corresponds to the sub-region part of the excel file. Column G of the JSR full extract
    start_date=models.DateTimeField('start_date') 
    apply_date=models.DateTimeField('apply_date')
    sector=models.CharField(max_length=200)
    def __unicode__(self):
    	return (self.title,self.description)
    
