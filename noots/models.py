from django.db import models

# Create your models here.

class IntroDescreption:
    
    def __init__(self, intro, slogan, title_for_mobile_app):
        self.intro :str = intro
        self.slogan: str = slogan
        self.title_for_mobile_app: str = title_for_mobile_app
        
        
class noots(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user_id = models.CharField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Users(models.Model):
    
    name = models.CharField()
    email = models.CharField()
    password = models.CharField()
    
    def __str__(self):
        return self.name
    
        
    
    
    