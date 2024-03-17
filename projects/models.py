from django.db import models

# relation to store user project data
class project_data( models.Model ):
    creater_id = models.IntegerField( )
    project_name = models.CharField( max_length = 100 )
    project_descript = models.TextField(  )
    end_date = models.DateField( )
    link = models.CharField(max_length = 100)
    tot_pos = models.IntegerField( )
    avl_pos = models.IntegerField( )


#project to rolls data
class project_roll_data( models.Model ):
    project_id = models.IntegerField( )
    roll_name = models.CharField( max_length = 200  )
    tot_pos = models.IntegerField( )
    avl_pos = models.IntegerField(  )

#project user data
class project_user( models.Model ):
    project_id = models.IntegerField( )
    enroller_id = models.IntegerField(  )
    roll_name = models.CharField( max_length = 200 )



#available rolls data
class rolls( models.Model ):
    roll_name = models.CharField( max_length = 200 )


#store the dynamic data of which project  by selected user from home page
class prj_client_machine( models.Model ):
    user_id = models.IntegerField( )
    project_id = models.IntegerField( )






