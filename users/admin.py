from django.contrib import admin
from .models import User, Player, Coach, LeagueOfficial
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role', 'phone_number', 'profile_picture')}),
    )
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')


admin.site.register(User, UserAdmin)
admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(LeagueOfficial)
