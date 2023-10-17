# from django.contrib import admin
# from .models import Demo, User
# # Register your models here.
# class DemoAdmin(admin.ModelAdmin):
#  list_display = all

# class UserAdmin(admin.ModelAdmin):
#  list_display=['id', 'fname', 'lname', 'email', 'password']

# # @admin.register(Demo)
# # @admin.register(User)
# @admin.register(Demo)
from django.contrib import admin
from .models import User
from .models import Demo
# from .models.category import Category
# from .models.customer import Customer

class AdminDemo(admin.ModelAdmin):
    list_display= ['mail']

class AdminUser(admin.ModelAdmin):
    list_display=['fname']


# Register your models here.
admin.site.register(User, AdminUser)
admin.site.register(Demo, AdminDemo)