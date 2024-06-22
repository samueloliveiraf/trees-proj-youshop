from django.contrib import admin
from .models import PlantedTree


@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tree', 'age', 'longitude', 'latitude', 'created_at', 'updated_at')
    list_filter = ('user', 'tree', 'created_at')
    search_fields = ('user__email', 'tree__name')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('user', 'tree', 'age')
        }),
        ('Location Information', {
            'fields': ('longitude', 'latitude')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        obj.clean()
        super().save_model(request, obj, form, change)

