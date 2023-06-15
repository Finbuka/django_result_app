from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
# from import_export import fields

# Register your models here.

from .models import Students, ResultU2018, ResultU2019
from import_export import resources



class CustomUserAdmin(ModelAdmin):
    list_display = ("first_name" ,"last_name" ,"email" ,"mat_number")


class CustomResultU2018(ImportExportModelAdmin):
    list_per_page = 100
    list_display = ("mat_number" ,"course_code" , "year", "semester", "grade")

class RoleResource(resources.ModelResource):
    
    class Meta:
        model = ResultU2019
        import_id_fields = ("mat_number","course_code")

class CustomResultU2019(ImportExportModelAdmin):
    resource_class = RoleResource

    # list_display = ("__str__",)
    # list_display_links = ()
    # list_filter = ()
    # list_select_related = False
    # list_per_page = 100
    # list_max_show_all = 200
    list_editable = ("course_code" , "year", "semester","mark", "grade")
    search_fields = ("mat_number","grade")
    search_help_text = None
    # date_hierarchy = None
    # save_as = False
    # save_as_continue = True
    # save_on_top = False
    # preserve_filters = True
    # inlines = ()

    # Custom templates (designed to be over-ridden in subclasses)
    # add_form_template = None
    # change_form_template = None
    # change_list_template = None
    # delete_confirmation_template = None
    # delete_selected_confirmation_template = None
    # object_history_template = None
    # popup_response_template = None

    # # Actions
    # actions = ()
    # action_form = helpers.ActionForm
    # actions_on_top = True
    # actions_on_bottom = False
    # actions_selection_counter = True
    # checks_class = ModelAdminChecks

    list_display = ("mat_number" ,"course_code" , "year", "semester","mark", "grade")



admin.site.register(Students, CustomUserAdmin)
admin.site.register(ResultU2018, CustomResultU2018)
admin.site.register(ResultU2019, CustomResultU2019)
