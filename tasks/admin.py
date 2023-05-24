from django.contrib import admin
from .models import Task


class TareaAdmin(admin.ModelAdmin):
    readonly_fields=('created', )
admin.site.register(Task, TareaAdmin)