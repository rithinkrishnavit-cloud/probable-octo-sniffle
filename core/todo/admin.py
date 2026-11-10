from django.contrib import admin
from .models import Todo


# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "create_at", "complete")
    list_editable = ("title",)

admin.site.register(Todo, TableAdmin)
