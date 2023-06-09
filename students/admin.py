from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.

from .models import Students, ResultU2018

class CustomUserAdmin(ModelAdmin):
    list_display = ("first_name" ,"last_name" ,"email" ,"mat_number")


class CustomResultAdmin(ModelAdmin):
    list_per_page = 500
    list_display = ("mat_number" ,"course_code" , "year", "semester", "grade")



admin.site.register(Students, CustomUserAdmin)
admin.site.register(ResultU2018, CustomResultAdmin)
