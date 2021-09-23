from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "date_created",
        "message",
    ]
