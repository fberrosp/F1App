from django.db import models
from django.db.models.fields import UUIDField, IntegerField, CharField, DateField, FloatField, TimeField


class Drivers(models.Model):
    driverId = CharField(max_length=255, primary_key=True, editable=False)
    number = IntegerField(blank=True, null=True)
    code = CharField(max_length=3, blank=True, null=True)
    forename = CharField(max_length=255)
    surname = CharField(max_length=255)
    dob = DateField()
    nationality = CharField(max_length=255)
    url = CharField(max_length=255)

    def __str__(self):
        return self.surname
