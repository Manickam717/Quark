from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from projects import models as proj_models
from user import models as user_models
from datetime import date
from home import models
import random

#list to store selected roles   
#role_selected = [ ]

# Create your views here.
@login_required
def home_page( request ):
    
    #activate the below command if you want create roll objects
    #instatiate_rolls( )
    
    user = request.user
    project_list = filtere_projects( user )
    rolls_obj = proj_models.rolls.objects.all( )
    
    if( request.method == 'GET' ):
        
        #delting all preselected roles of the user
        models.roles_selected.objects.filter( user_id = user.id ).delete( )
        
        return render( request  ,'home.html' ,{ 'rolls_objects' : rolls_obj ,
                                                'roles_selected' :[ ],
                                                'project_objects'  : project_list,  }  )  
    
    else:
        if(  'clear_screen'  in request.POST ) :
            objs = models.roles_selected.objects.filter( user_id = user.id )
            objs.delete()    
            return render( request  ,'home.html' ,{ 'rolls_objects' : rolls_obj ,
                                                    'roles_selected' :[ ],
                                                    'project_objects'  : project_list,  }  )  
        
        else:
            role = request.POST[ 'role' ]
            print( f"home_page {role}" )
            
            if( role in models.roles_selected.objects.filter( user_id = user.id).values_list( 'selected_role' ,flat=True ) ):
                obj = models.roles_selected.objects.get( user_id = user.id ,selected_role = role )
                obj.delete()
                        
            else:
                obj = models.roles_selected( user_id = user.id ,selected_role = role )
                obj.save( )
            
            role_selected = models.roles_selected.objects.filter( user_id = user.id).values_list( 'selected_role' ,flat=True )
            
            if( len( role_selected ) > 0 ):
                projects_filtered = fiter_based_on_role(  project_list ,role_selected )
                return render( request  ,'home.html' ,{ 'rolls_objects' : rolls_obj ,
                                                        'roles_selected' :role_selected,
                                                        'project_objects'  : projects_filtered, })
            
            else:
                return render( request  ,'home.html' ,{ 'rolls_objects' : rolls_obj ,
                                                        'roles_selected' :[ ],
                                                        'project_objects'  : project_list,  })
                
                
#filtering projects based on basic constrains
def filtere_projects( user_obj ) : 
    current_date = date.today( )

    #folter list of projects with end date greater than equal to current date ,and has vacancy
    project_objs = proj_models.project_data.objects.exclude( creater_id = user_obj.id  ).filter(  end_date__gte=current_date 
                                                            ,avl_pos__gt=0  )
    
    #list of project ids enrolled by user
    user_erl_pro_ids = proj_models.project_user.objects.filter( enroller_id = user_obj.id ).values_list('project_id', flat=True).distinct()


    #list contians project_creater object recommended
    proj_list = [ ]

    #iterating to finf list of projects not enrolled by user
    for prj in project_objs :
        if(  prj.id  not in  user_erl_pro_ids ) : 
            
            creater_name = User.objects.get(  id  = prj.creater_id  ).username

            project_crt_obj = models.project_creater(   project_id = prj.id , 
                                                       project_name = prj.project_name ,
                                                       project_descript = prj.project_descript ,
                                                       creater_name = creater_name   )
            
            proj_list.append( project_crt_obj )
    
    return proj_list  


#filter a project based on roles
def fiter_based_on_role(  intial_project_list ,roles_selected ):
    
    print( roles_selected )
    #filtering ids of the projects which vaccances for given rolls
    project_ids = proj_models.project_roll_data.objects.filter(  roll_name__in = roles_selected 
                                                                , avl_pos__gt = 0 ).values_list('project_id', flat=True).distinct()
    
    print( project_ids )
    
    #list stores the objects of filtered projects
    filtered_proj_list = [ ]

    #sfiltering project objects which has vaccancys for given rolls
    for obj in intial_project_list:
        if( obj.project_id in  project_ids  ):
            filtered_proj_list.append(  obj )

    print(  filtered_proj_list )
    
    return filtered_proj_list


#used to instatiate rolls from scratch
def instatiate_rolls( ):
    roles = [
    "Software Engineer",
    "Data Scientist",
    "Machine Learning Engineer",
    "Python Developer",
    "Full Stack Developer",
    "Web Developer",
    "Data Analyst",
    "DevOps Engineer",
    "AI Engineer",
    "Computer Vision Engineer",
    "Natural Language Processing (NLP) Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Game Developer",
    "Cloud Engineer",
    "Cybersecurity Analyst",
    "Robotics Engineer",
    "Bioinformatics Scientist",
    "Quantitative Analyst",
    "Systems Engineer",
    "Embedded Systems Engineer",
    "Automation Engineer",
    "Data Engineer",
    "Software Architect",
    "Research Scientist",
    "Mobile App Developer",
    "Cryptographer",
    "Blockchain Developer",
    "Computer Graphics Programmer",
    "High-Performance Computing (HPC) Engineer",
    "Network Engineer",
    "Compiler Engineer",
    "Scientific Programmer",
    "Algorithm Engineer",
    "Computational Linguist",
    "GIS Analyst",
    "Financial Engineer",
    "Test Automation Engineer",
    "UX/UI Developer",
    "Game AI Programmer",
    "Software Development Manager",
    "Technical Lead",
    "Big Data Engineer",
    "Cloud Solutions Architect",
    "System Administrator",
    "Mobile Game Developer",
    "Digital Signal Processing (DSP) Engineer",
    "Software Quality Assurance Engineer",
    "Data Visualization Engineer",
    "Database Administrator",
    "Quantum Computing Scientist",
    "Virtual Reality Developer",
    "Augmented Reality Developer",
    "IoT Developer",
    "Backend Systems Developer",
    "Chatbot Developer",
    "Computer Science Professor",
    "Technology Consultant",
    "Technical Writer",
    "IT Project Manager",
    "IT Security Specialist",
    "IT Support Engineer",
    "IT Auditor",
    "IT Compliance Analyst",
    "IT Business Analyst",
    "IT Systems Analyst",
    "IT Trainer",
    "IT Sales Engineer",
    "IT Recruiter",
    "IT Procurement Specialist",
    "IT Risk Analyst",
    "IT Operations Manager",
    "IT Service Desk Manager",
    "IT Director",
    "IT Vice President",
    "IT Chief Information Officer (CIO)",
    "IT Chief Technology Officer (CTO)",
    "IT Chief Security Officer (CSO)",
    "IT Chief Data Officer (CDO)",
    "IT Chief Digital Officer (CDO)",
    "IT Chief Operating Officer (COO)",
    "IT Chief Financial Officer (CFO)",
    "IT Chief Executive Officer (CEO)",
    "IT Project Coordinator",
    "IT Project Analyst",
    "IT Project Leader",
    "IT Project Administrator",
    "IT Project Assistant",
    "IT Project Support",
    "IT Project Planner",
    "IT Project Scheduler",
    "IT Project Controller",
    "IT Project Manager Assistant",
    "IT Project Manager Trainee",
    "IT Project Manager Intern",
    "IT Project Manager Associate",
    "IT Project Manager Specialist",
    "IT Project Manager Expert",
    "IT Project Manager Consultant",
    "IT Project Manager Advisor" ]
    
    for role in roles:
        obj = proj_models.rolls( roll_name = role )
        obj.save( )
        
        















    

