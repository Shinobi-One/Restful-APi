# pylint: disable=import-error
from django.contrib import admin
from app.models import stuff1,collection
# Register your models here.
class show(admin.ModelAdmin):
    admin.site.register(stuff1,),
    admin.site.register(collection,)