from django.db import models
from utils.snippets import autoslugFromUUID


@autoslugFromUUID()
class Todo(models.Model):
    task = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=254)
    details = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("Todo")
        verbose_name_plural = ("Todos")
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.task
