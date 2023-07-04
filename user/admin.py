from django.contrib import admin
from .models import RegularUserModel, FieldOfStudy, Subjects, Modules
# Register your models here.

admin.site.register(RegularUserModel)
admin.site.register(FieldOfStudy)
admin.site.register(Subjects)
admin.site.register(Modules)
