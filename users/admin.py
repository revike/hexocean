from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import HexUser, RateUser


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rate', {'fields': (
            'rate', )}),
    )

admin.site.register(HexUser, CustomUserAdmin)
admin.site.register(RateUser)
