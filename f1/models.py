from django.db import models
from django.db.models.fields import UUIDField, IntegerField, CharField, DateField, FloatField, TimeField

class Drivers(models.Model):
    driverId = UUIDField(primary_key=True, editable=False)
    driverRef = CharField(max_length=255)
    number = IntegerField(max_length=11)
    code = CharField(max_length=3)
    forename = CharField(max_length=255)
    surname = CharField(max_length=255)
    dob = DateField()
    nationality = CharField(max_length=255)
    url = CharField(max_length=255)

    def __str__(self):
        return self.surname