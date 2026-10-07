from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("subject", "rating", "class_name", "created_at")
    list_filter = ("subject", "rating", "created_at")
    search_fields = ("name", "class_name", "subject", "comment")
