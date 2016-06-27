from django.contrib import admin
from .models import School, Program, Student, SchoolProgram, Application


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','abbr','greverbal','greapti','grewriting','gpa']
admin.site.register(School, SchoolAdmin)

class ProgramAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level','greverbal','greapti','grewriting','gpa']
admin.site.register(Program, ProgramAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'current_program', 'current_gpa', 'current_credit_hours', 'current_start_date', 'current_end_date'
                    ,'prev_program','prev_gpa','prev_credit_hours','prev_start_date','prev_end_date']
admin.site.register(Student, StudentAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id','student','date_submitted','date_updated','school_program']
admin.site.register(Application, ApplicationAdmin)

class SchoolProgramAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'program','greverbal','greapti','grewriting','gpa']
admin.site.register(SchoolProgram, SchoolProgramAdmin)



