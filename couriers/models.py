from django.db import models


class Courier(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CourierOrder(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Courier: {self.courier.name}, Order: {self.order.id}"
