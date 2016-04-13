from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ShinyApp(models.Model):
    shiny_name = models.CharField(max_length=200)
    shiny_description = models.CharField(max_length=200, default='')
    shiny_show = models.BooleanField(default=True)
    def __str__(self):
        return self.shiny_name
    def is_showed(self):
        return self.shiny_show
    def show_desc(self):
        return self.shiny_description
