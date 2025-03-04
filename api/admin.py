from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Note  # Replace with your actual model

class YourModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser  # ✅ Only superusers can add

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # ✅ Only superusers can edit

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # ✅ Only superusers can delete

admin.site.register(Note, YourModelAdmin)
