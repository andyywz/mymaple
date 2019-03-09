import datetime

from django.db import models
from django.utils import timezone

class Daily(models.Model):
    title = models.CharField(max_length=200, blank=False)
    desc = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('-completed', 'title')

    def __str__(self):
        completed = ' done' if not self.is_stale else ''
        return self.title + completed

    def reset(self):
        self.completed = False
        self.completed_at = None
        self.save()

    def complete(self):
        self.completed = True
        self.completed_at = timezone.now()
        self.save()

    def is_stale(self):
        if self.completed_at:
            return self.completed_at.date() != timezone.now().date()
        else:
            return True
