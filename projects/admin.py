from django.contrib import admin
from . import models

# Register your models here.
admin.site.register( models.project_data )
admin.site.register( models.project_roll_data )
admin.site.register( models.project_user )