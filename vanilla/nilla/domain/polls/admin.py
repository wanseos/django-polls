from django.contrib import admin

from .models import Question, QuestionChoice


class QuestionChoiceInline(admin.StackedInline):
    model = QuestionChoice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {"fields": ["question_text"]},
        ),
        (
            "Date information",
            {"fields": ["pub_date"], "classes": ["collapse"]},
        ),
    ]
    inlines = [QuestionChoiceInline]
    list_display = ["question_text", "pub_date"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


def register_polls_admin():
    admin.site.register(Question, QuestionAdmin)
