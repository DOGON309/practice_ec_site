import uuid
from django.db import models
from user.models import User
from products.models import Product

class Order(models.Model):
    STATUS = (
        ('new', '新規'),
        ('shipped', '発送済み'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    status = models.CharField(max_length=255, choices=STATUS)

    def __str__(self) -> str:
        return self.name
    
class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    subtotal = models.IntegerField()

    def __str__(self) -> str:
        return self.order_id