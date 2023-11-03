from django.contrib import admin
from .models import User
# Register your models here.
from .models import registerecandidates,CandidateForm,EducationalDetailsForm


class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields = ('name','email')


admin.site.register(User, UserAdmin)

admin.site.register(registerecandidates)

admin.site.register(CandidateForm)

admin.site.register(EducationalDetailsForm)