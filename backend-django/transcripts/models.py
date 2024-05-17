from django.db import models
from django.core.serializers.json import DjangoJSONEncoder

NULLABLE = {"null": True, "blank": True}
DEFAULT_CHAR = {"max_length": 255}


# Create your models here.
class Transcript(models.Model):
    title = models.CharField(**DEFAULT_CHAR, **NULLABLE)
    date = models.DateTimeField(**NULLABLE, default=None)
    duration = models.IntegerField(**NULLABLE)
    summary = models.JSONField(**NULLABLE, encoder=DjangoJSONEncoder)
    video_url = models.TextField(**NULLABLE)


class Sentence(models.Model):
    index = models.IntegerField(**NULLABLE, db_index=True)
    text = models.TextField(**NULLABLE)
    start_time = models.CharField(**NULLABLE, **DEFAULT_CHAR)
    end_time = models.CharField(**NULLABLE, **DEFAULT_CHAR)
    speaker_id = models.CharField(**NULLABLE, **DEFAULT_CHAR)
    speaker_name = models.CharField(**NULLABLE, **DEFAULT_CHAR)
    transcript = models.ForeignKey(
        Transcript, on_delete=models.CASCADE, related_name="sentences"
    )

    class Meta:
        ordering = ["index"]
