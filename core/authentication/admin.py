from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ('id','first_name', 'last_name', 'email', 'phone_number')
    date_hierarchy = 'date_joined'
    ordering = ('-id',)


    fieldsets = (
        (
            ('User and Pass'), {
                'fields':('username', 'password')
            }
        ),
        (
            ('User Info'), {
                'fields':('first_name', 'last_name', 'email', 'phone_number')
            }
        ),
        (
            ('Metadata'), {
                'fields':( 'last_login', 'date_joined')
            }
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)