from django.db import models
from django.db.models import ForeignKey, AutoField
from django.db.models.fields import IntegerField, CharField, DateField, FloatField, TimeField


class Drivers(models.Model):
    driverId = CharField(max_length=255, primary_key=True, editable=False)
    permanentNumber = IntegerField(blank=True, null=True)
    code = CharField(max_length=3, blank=True, null=True)
    givenName = CharField(max_length=255)
    familyName = CharField(max_length=255)
    dateOfBirth = DateField()
    nationality = CharField(max_length=255)
    url = CharField(max_length=255)

    def __str__(self):
        return self.surname


class Constructors(models.Model):
    constructorId = CharField(max_length=255, primary_key=True, editable=False)
    name = CharField(max_length=255)
    nationality = CharField(max_length=255)
    url = CharField(max_length=255)

    def __str__(self):
        return self.name


class Circuits(models.Model):
    circuitId = CharField(max_length=255, primary_key=True, editable=False)
    name = CharField(max_length=255)
    location = CharField(max_length=255)
    country = CharField(max_length=255)
    lat = FloatField()
    lng = FloatField()
    url = CharField(max_length=255)

    def __str__(self):
        return self.name


class Seasons(models.Model):
    year = IntegerField(primary_key=True, editable=False)
    url = CharField(max_length=255)

    def __str__(self):
        return self.year


class Races(models.Model):
    raceId = AutoField(primary_key=True)
    season = ForeignKey(Seasons, on_delete=models.CASCADE)
    round = IntegerField()
    raceName = CharField(max_length=255)
    circuitId = ForeignKey(Circuits, on_delete=models.CASCADE)
    circuitName = CharField(max_length=255)
    date = DateField()
    country = CharField(max_length=255)
    lat = FloatField()
    lng = FloatField()
    url = CharField(max_length=255)


class Qualifyings(models.Model):
    qualifyId = AutoField(primary_key=True)
    season = IntegerField()
    round = IntegerField()
    forename = CharField(max_length=255)
    surname = CharField(max_length=255)
    code = CharField(max_length=255)
    number = IntegerField()
    qualifyingTime = TimeField()
    grid = IntegerField()
    car = CharField(max_length=255)


class Results(models.Model):
    resultId = AutoField(primary_key=True)
    season = IntegerField()
    round = IntegerField()
    circuitId = CharField(max_length=255)
    driverId = ForeignKey(Drivers, on_delete=models.CASCADE)
    dob = DateField()
    nationality = CharField(max_length=255)
    constructorId = ForeignKey(Constructors, on_delete=models.CASCADE)
    grid = IntegerField()
    time = IntegerField()
    status = CharField(max_length=255)
    points = FloatField()
    position = IntegerField()


class DriverStandings(models.Model):
    driverStandingsId = AutoField(primary_key=True)
    season = IntegerField()
    round = IntegerField()
    driverId = ForeignKey(Drivers, on_delete=models.CASCADE)
    points = FloatField()
    wins = IntegerField()
    position = IntegerField()


class ConstructorStandings(models.Model):
    constructorStandingsId = AutoField(primary_key=True)
    season = IntegerField()
    round = IntegerField()
    constructorId = ForeignKey(Constructors, on_delete=models.CASCADE)
    points = FloatField()
    wins = IntegerField()
    position = IntegerField()
