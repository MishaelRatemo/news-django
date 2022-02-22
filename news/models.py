import email
from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering=['first_name']
    
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
