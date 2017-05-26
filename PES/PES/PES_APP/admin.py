# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Profile_user

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    # fields = (
    #     )
    model = Profile

    list_display = (
        'user',
        'get_name',
        'document_number',
        'gender',
        'phone',
        'service_ce',
        'service_plo',
        'service_car',
        'service_elec',
        'service_jar',
        'service_pin',
        'service_pla',
        'service_techo',
        'service_par',
        'address',
        'availability_monday',
        'availability_tuesday',
        'availability_wednesday',
        'availability_thursday',
        'availability_friday',
        'availability_saturday',
        'availability_sunday',
        'certified',
        'role'
    )

    def get_name(self, obj):
        return obj.user.first_name+" "+obj.user.last_name
    get_name.admin_order_field = 'user'  
    get_name.short_description = 'Name'  

admin.site.register(Profile, ProfileAdmin)

class ProfileUserAdmin(admin.ModelAdmin):
    # fields = (
    #     )
    model = Profile_user

    list_display = (
        'user',
        'get_name',
        'document_number',
        'gender',
        'phone',
        'role',
        'payment',
        'address',
        'city'
    )

    def get_name(self, obj):
        return obj.user.first_name+" "+obj.user.last_name
    get_name.admin_order_field = 'user'  
    get_name.short_description = 'Name'  

admin.site.register(Profile_user, ProfileUserAdmin)