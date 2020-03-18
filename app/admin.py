from django.contrib import admin
from .models import Goals
# Register your models here.

class GoalsAdmin(admin.ModelAdmin):
    search_fields = ["goal"]
    list_filter = ["goal"]
    list_display = [
        "pk",       
        "goal",
    ]
    list_editable = ["goal"]

admin.site.register(Goals,GoalsAdmin)