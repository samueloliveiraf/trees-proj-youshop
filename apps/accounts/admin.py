from django.contrib import admin
from .models import Account, User


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'account', 'is_admin')
    search_fields = ('user__email', 'account__email')
