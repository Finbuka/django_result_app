from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Students, ResultU2018, ResultU2019, ResultU2020
from import_export import resources


@admin.register(Students)
class CustomUserAdmin(ModelAdmin):
    list_display = ("first_name" ,"last_name" ,"email" ,"mat_number")


class RoleResource2018(resources.ModelResource):
    class Meta:
        model = ResultU2018
        import_id_fields = ("mat_number","course_code")

@admin.register(ResultU2018)
class CustomResultU2018(ImportExportModelAdmin):
    resource_class = RoleResource2018
    list_editable = ("course_code" , "year", "semester","mark", "grade")
    search_fields = ("mat_number","grade")
    list_display = ("mat_number" ,"course_code" , "year", "semester","mark", "grade")


class RoleResource2019(resources.ModelResource):
    class Meta:
        model = ResultU2019
        import_id_fields = ("mat_number","course_code")

@admin.register(ResultU2019)
class CustomResultU2019(ImportExportModelAdmin):
    resource_class = RoleResource2019
    list_editable = ("course_code" , "year", "semester","mark", "grade")
    search_fields = ("mat_number","grade")
    list_display = ("mat_number" ,"course_code" , "year", "semester","mark", "grade")

class RoleResource2020(resources.ModelResource):
    class Meta:
        model = ResultU2020
        import_id_fields = ("mat_number","course_code")

@admin.register(ResultU2020)
class CustomResultU2019(ImportExportModelAdmin):
    resource_class = RoleResource2020
    list_editable = ("course_code" , "year", "semester","mark", "grade")
    search_fields = ("mat_number","grade")
    list_display = ("mat_number" ,"course_code" , "year", "semester","mark", "grade")

