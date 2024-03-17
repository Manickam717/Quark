from django.shortcuts import render ,redirect
from django.http import HttpResponse
from . import models
from projects import models as projmodel
from datetime import date
import json


def add_project( request ) :
    
    rolls_obj = projmodel.rolls.objects.all( )
    
    if( request.method == 'GET'):
        return  render( request ,'project_creation.html' ,{ 'roles_objs' : rolls_obj } )
    
    else:
        if( request.body != None ):
            #fetching the data from request
            json_data = json.loads( request.body )
            
            #calculate the total_position available 
            tot_pos = 0
            for role_obj in json_data['selectedRoles'] :
                tot_pos = tot_pos + int( role_obj['memberCount'] )
                
                
            #instantiating project data object
            prjt_data_object = projmodel.project_data( creater_id = request.user.id ,
                                                       project_name = json_data['projectTitle'],
                                                       project_descript = json_data['projectDescription'],
                                                       end_date = json_data['endDate'] ,
                                                       link = json_data['link'] ,
                                                       tot_pos = tot_pos ,
                                                       avl_pos = tot_pos )
            
            prjt_data_object.save( )
            
            #instatiating rolls data for the project 
            for role_obj in json_data['selectedRoles']:
                projmodel.project_roll_data( project_id = prjt_data_object.id ,
                                             roll_name = role_obj['role'] ,
                                             tot_pos = int( role_obj['memberCount'] ),
                                             avl_pos = int( role_obj['memberCount'] ) ).save()
            
            return HttpResponse( "sucessfull" )    
        else:
            return HttpResponse( "unsucessfull" )
        
def enroll_project( request ):
    
    user = request.user
    
    if( request.method == 'GET' ):
        
        #deleting old project-client mch data
        projmodel.prj_client_machine.objects.filter( user_id = request.user.id ).delete( )
        
        #updating new data
        prjct_id = int( request.GET[ 'project_id' ] )
        projmodel.prj_client_machine( user_id = request.user.id,
                                      project_id = prjct_id ).save()
        
        
        project_obj = projmodel.project_data.objects.get( id = prjct_id )
         
        if( not check_accesibility( user ,project_obj ) ):
            return redirect( '/')
        
        role_objs = projmodel.project_roll_data.objects.filter( project_id = prjct_id,
                                                               avl_pos__gt = 0 )
        
        return render( request , 'project_enroll.html' ,{ 'project_obj' : project_obj , 
                                                          'role_objs' : role_objs } )
    
    else:
        enroller_id = user.id 
        roll_name = request.POST[ 'role' ]
        prjct_id = projmodel.prj_client_machine.objects.get( user_id = request.user.id ).project_id
        
        # decreasing avl_pos by one in prj_rll_data
        obj = projmodel.project_roll_data.objects.get( roll_name = roll_name , project_id = prjct_id)
        obj.avl_pos = obj.avl_pos - 1 
        obj.save( )
        ######
        
        #decreasing avl_pos by one in prjectdata
        obj = projmodel.project_data.objects.get( id = prjct_id )
        obj.avl_pos = obj.avl_pos - 1 
        obj.save( )
        #####
        
        #updating prj_user data
        projmodel.project_user( project_id = prjct_id , 
                               enroller_id = enroller_id , 
                               roll_name = roll_name ).save( )
        
        return redirect( '/' )
        
def check_accesibility( user_obj  ,project_obj ):
    
    if(  project_obj.avl_pos > 0 and  project_obj.end_date >= date.today( )  and  project_obj.creater_id != user_obj.id  ) :
          
        if( not models.project_user.objects.filter(  project_id = project_obj.id  ,enroller_id = user_obj.id ) .exists( ) ):
            
            return True
        else:  
            return False
   
    else:
        return False
    
             
            



