from django.contrib import admin

# Register your models here.
from .models import users
admin.site.register(users)
from .models import FormModel
admin.site.register(FormModel)