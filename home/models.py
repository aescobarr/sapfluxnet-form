from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ShinyApp(models.Model):
    shiny_name = models.CharField(max_length=200)
    shiny_description = models.CharField(max_length=200, default='')
    shiny_show = models.BooleanField(default=True)
    shiny_address = models.URLField(max_length=200, default='')
    def __str__(self):
        return self.shiny_name
    def is_showed(self):
        return self.shiny_show
    def show_desc(self):
        return self.shiny_description
    def show_url(self):
        return self.shiny_address

class SfnTeam(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, default='')
    web = models.URLField(max_length=200, default='')
    affil = models.CharField(max_length=200, default='CREAF')
    courtesy = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.name
    def getEmail(self):
        return self.email
    def getWeb(self):
        return self.web
    def getAffil(self):
        return self.affil
    def getCourtesy(self):
        return self.courtesy
