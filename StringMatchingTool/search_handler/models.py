# models.py
from django.db import models
import uuid

class FileProcessingResult(models.Model):
    result_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    query = models.CharField(max_length=255)
    results = models.JSONField()  # or use TextField if you prefer JSON serialization

    def __str__(self):
        return str(self.result_id)
