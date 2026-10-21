from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0002_feedback_clarity_rating_and_participation_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="teacher",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
