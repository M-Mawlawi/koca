from django.contrib import admin
from .models import Answers, Question,Exam,Users,SlideShow
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class QuestionAdmin(ImportExportModelAdmin):
    list_display = ['question']

class ExamAdmin(admin.ModelAdmin):
    list_display = ['username','created_at']
    def username(self,object):
        return object.user_id.username

class SlideShowAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(ImportExportModelAdmin):
    list_display = ['answer']

class ContactInline(admin.StackedInline):
    model = Users
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin(UserAdmin) :
    inlines = (ContactInline, )

class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question,QuestionAdmin)
admin.site.register(Exam,ExamAdmin)
admin.site.register(Answers,AnswerAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(SlideShow, SlideShowAdmin)