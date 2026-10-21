from rest_framework import serializers

from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            "id",
            "name",
            "class_name",
            "subject",
            "teacher",
            "rating",
            "clarity_rating",
            "participation_rating",
            "comment",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
        extra_kwargs = {
            "teacher": {"required": True, "allow_null": False, "allow_blank": False},
            "clarity_rating": {"required": True, "allow_null": False},
            "participation_rating": {"required": True, "allow_null": False},
        }

    def validate_rating(self, value):
        return self._validate_rating(value)

    def validate_clarity_rating(self, value):
        return self._validate_rating(value)

    def validate_participation_rating(self, value):
        return self._validate_rating(value)

    def _validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Hinne peab olema vahemikus 1–5.")
        return value
