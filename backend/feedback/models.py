from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    class_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=120)
    teacher = models.CharField(max_length=120, null=True, blank=True)
    rating = models.PositiveSmallIntegerField()
    clarity_rating = models.PositiveSmallIntegerField(null=True)
    participation_rating = models.PositiveSmallIntegerField(null=True)
    comment = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} ({self.rating}/5)"
