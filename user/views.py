from django.shortcuts import render
from django.contrib.auth.models import User
from projects import models as proj_models
from user import models as user_model


# Create your views here.
def profile_page(request):
    
    auth_user_obj = request.user #geting personal data from auth_user
    
    user_data_obj = user_model.user_data.objects.get( id = auth_user_obj.id ) 
    
    
    #list of projects enrolled by user    
    enroll_obj_list  = enrolled_project_list( auth_user_obj )
    enroll_obj_list.reverse( )
    
    #list of projects created by user
    created_obj_list = created_project_list( auth_user_obj )
    created_obj_list.reverse( )
    
    return render( request ,'profile.html' , { 'auth_user' : auth_user_obj ,
                                               'user_data_obj' : user_data_obj ,
                                               'created_projects':created_obj_list ,
                                               'enrolled_projects':enroll_obj_list } ) 
                                                   
#filters the proejcts enrolled by the user
def enrolled_project_list( user_obj ):

    #filter ids of projects enroledd
    prj_enl_ids = proj_models.project_user.objects.filter(enroller_id=user_obj.id).values_list('project_id',flat=True).distinct()
     
    #filtering project objects
    project_obj = proj_models.project_data.objects.filter( id__in = prj_enl_ids )

    #list to store enroll objects
    enroll_obj_list =[  ]

    for obj in project_obj :
    
        #userroll extraction
        roll_name = proj_models.project_user.objects.get(  project_id = obj.id ,enroller_id = user_obj.id ).roll_name 

        #instaiting obj 
        prj_obj = user_model.enrolled_project(  
                           project_name = obj.project_name , 
                           project_descript = obj.project_descript ,
                           link = obj.link ,
                           roll_name = roll_name )
        
        enroll_obj_list.append( prj_obj )
    

    return enroll_obj_list

#fetching info projects created by user
def created_project_list( user_obj ):

    #filter ids of projects created
    prj_created_objs = proj_models.project_data.objects.filter(creater_id=user_obj.id)
    
    return prj_created_objs
    
    
