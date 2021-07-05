from App1.models import Contactdata,Blog
from django.contrib import admin

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','message']

class BlogAdmin(admin.ModelAdmin):
    list_display=['title','posted_date','author']
    


admin.site.register(Contactdata,ContactAdmin)
admin.site.register(Blog,BlogAdmin)
