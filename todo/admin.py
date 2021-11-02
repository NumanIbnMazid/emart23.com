from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ["task", "slug", "is_completed", "created_at", "updated_at"]
    
    class Meta:
        model = Todo
        
admin.site.register(Todo, TodoAdmin)
