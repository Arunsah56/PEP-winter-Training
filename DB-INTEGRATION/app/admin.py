from django.contrib import admin

# Register your models here.
from .models import Class, Driver, Car, student, parent, arun_info

admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Class)
admin.site.register(parent)
admin.site.register(student)
admin.site.register(arun_info)