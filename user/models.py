from django.db import models

# Create your models here.
class user_data(models.Model):
    institution = models.CharField(max_length = 200)
    dept = models.CharField(max_length = 50)
    year = models.IntegerField()
    number = models.CharField( max_length = 15 )

class enrolled_project:
    def __init__( self ,project_name ,project_descript ,link ,roll_name ):
        self.project_name = project_name
        self.project_descript = project_descript
        self.link = link 
        self.roll_name = roll_name

