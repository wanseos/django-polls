from django.contrib import admin

from .models import polls_models

admin.site.register(polls_models.Question)
