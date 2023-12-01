
from django.contrib import admin

from .models import Class, Enrollment, Major, Student

# Register your models here.
admin.site.register(Major)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Enrollment)
