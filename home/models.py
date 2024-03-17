from django.db import models

# Create your models here.
class project_creater :
    
    def __init__( self ,project_id ,project_name ,creater_name ,project_descript):
        self.project_id = project_id
        
        self.project_name = project_name
        
        self.project_descript = project_descript
        
        self.creater_name = creater_name
    
    def __str__(self) :
        print( self.project_id )
        print( self.project_name  )
        print( self.project_descript)
        print( self.creater_name )

class roles_selected( models.Model ):
    user_id = models.IntegerField( )
    selected_role = models.CharField( max_length = 200 )
        


