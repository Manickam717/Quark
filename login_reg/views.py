from django.shortcuts import render ,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from user.models import user_data

# login view
def login( request ):
    if(request.method == 'GET'):
        return render(request,'login_index1.html')
    else:
        user_name = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username = user_name,password = password)

        if( user != None ):
            auth.login( request  ,user )
            return redirect( '/')
        else:
            return render(request,'login_index1.html')

# registeration view
def register( request ):
    if( request.method == 'GET' ):
        print( 'register get request ')
        return render( request ,'register_index.html')

    else:
        first_name = request.POST[ 'first_name' ]
        last_name = request.POST[ 'last_name' ]
        username = request.POST[ 'username' ]
        email = request.POST['email']
        institute_name = request.POST[ 'institute_name' ]
        dept = request.POST[ 'dept' ]
        year = request.POST[ 'year' ]
        number = request.POST[ 'number']

        password = request.POST[ 'password' ]
        confirmpassword = request.POST[ 'conf_password' ]

        if( password == confirmpassword ):

            if( User.objects.filter( username = username).exists( ) ):
                return render( request ,'register_index.html')
            
            elif( User.objects.filter( email = email).exists( ) ):
                return render( request ,'register_index.html')
            
            else:
                auth_user_obj = User.objects.create_user( first_name = first_name,
                                                last_name = last_name,
                                                username = username,
                                                email = email,
                                                password = password,
                                                )
                user_data_obj = user_data(  institution = institute_name , 
                                            dept = dept , 
                                            year = year ,
                                            number = number )
                
                
                user_data_obj.save( )
                auth_user_obj.save( )
                authenticate_user = auth.authenticate( username = username ,password = password )
                auth.login( request ,authenticate_user )

                return redirect( '/' )
            

        

        

    
