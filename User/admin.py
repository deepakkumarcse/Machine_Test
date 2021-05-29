from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email')
    search_fields = ['email', 'username']
    exclude = ('groups', 'user_permissions', 'last_login')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
