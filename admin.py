from django.contrib import admin

# Register your models here.

from .models import SupplementaryQuestion, SupplementaryQuestionAnswer, Application, College, Participates_In, Extracurriculars, Student, Guidance_Counselor

admin.site.register(SupplementaryQuestion)
admin.site.register(SupplementaryQuestionAnswer)
admin.site.register(Application)
admin.site.register(College)
admin.site.register(Participates_In)
admin.site.register(Extracurriculars)
admin.site.register(Student)
admin.site.register(Guidance_Counselor)