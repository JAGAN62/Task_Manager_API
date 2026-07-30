from django.contrib import admin

from .models import Task


@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "owner",
        "priority",
        "status",
        "created_at",
    )

    list_filter = (
        "priority",
        "status",
    )

    search_fields = (
        "title",
        "description",
    )