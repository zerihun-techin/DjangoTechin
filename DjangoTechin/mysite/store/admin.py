from django.contrib import admin
from . models import shop
from polls.models import *
# Register your models here.


admin.site.register(shop)
admin.site.register(Question)