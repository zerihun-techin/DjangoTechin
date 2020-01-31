from django.contrib import admin
from .models  import  *
from  . import models as md

# Register your models here.


admin.site.register(md.Question)
