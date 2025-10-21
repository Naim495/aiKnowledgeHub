from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class KnowledgeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='knowledge_entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
