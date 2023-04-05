from django.db import models

# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    unit = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]