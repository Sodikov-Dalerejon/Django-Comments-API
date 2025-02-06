from django.db import models

class UserText(models.Model):
    username = models.CharField(max_length=150, unique=True)
    textbox = models.TextField()
    
    def __str__(self):
        return self.username
