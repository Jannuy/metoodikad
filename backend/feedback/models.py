from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    class_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=120)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} ({self.rating}/5)"
