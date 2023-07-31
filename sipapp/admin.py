from django.contrib import admin
from .models import Student
admin.site.site_header= "Sipalaya Info Tech"
admin.site.index_title= "Sipalaya"

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']