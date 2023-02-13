from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import User



@admin.register(User)
class UserAdmin(BaseAdmin):
	add_fieldsets = (
        (None, { 'fields':('username','email','first_name','password1','password2')}),
    )

