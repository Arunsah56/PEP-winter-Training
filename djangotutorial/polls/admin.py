from django.contrib import admin
from .models import users, FormModel, LoginUser, SingupUser
# Register your models here.

admin.site.register(users)

admin.site.register(FormModel)

admin.site.register(LoginUser)

admin.site.register(SingupUser)
