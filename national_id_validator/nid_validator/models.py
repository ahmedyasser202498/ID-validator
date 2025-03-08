from django.db import models

class APIKey(models.Model):
    key = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.key
