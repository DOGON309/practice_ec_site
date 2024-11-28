import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.name