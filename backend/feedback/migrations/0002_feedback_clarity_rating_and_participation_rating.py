from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="clarity_rating",
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="feedback",
            name="participation_rating",
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
