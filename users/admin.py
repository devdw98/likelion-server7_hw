from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser

# Register your models here.

class CustomerUserAdmin(UserAdmin):
    model = CustomerUser
    list_display = ['email', 'name']

admin.site.register(CustomerUser, CustomerUserAdmin)