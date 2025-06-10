from django.db import models

# Create your models here.

class IntroDescreption:
    
    def __init__(self, intro, slogan, title_for_mobile_app):
        self.intro :str = intro
        self.slogan: str = slogan
        self.title_for_mobile_app: str = title_for_mobile_app
        
        
class noots:
    def __init__(self, noots_title, text):
        self.title = noots_title
        self.text = text
        
    
    
    