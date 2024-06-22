from django.contrib import admin
from .models import Tree


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'scientific_name', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'scientific_name')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'scientific_name')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
