from typing import ClassVar
from django.contrib import admin
from django.db import models
from . import models


@admin.register(models.message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "organization",
        "email",
        "phone_number",
        "date_created",
        "message",
    ]
