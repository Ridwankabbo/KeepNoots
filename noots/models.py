from django.db import models

# Create your models here.

class IntroDescreption:
    
    def __init__(self, intro, slogan, title_for_mobile_app):
        self.intro :str = intro
        self.slogan: str = slogan
        self.title_for_mobile_app: str = title_for_mobile_app
        
    
    
    