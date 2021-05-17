# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Flightdata(models.Model):
    airline = models.CharField(max_length=3, blank=True, null=True)
    airlineid = models.CharField(db_column='airlineId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sourceairport = models.CharField(db_column='sourceAirport', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sourceairportid = models.CharField(db_column='sourceAirportId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    destinationairport = models.CharField(db_column='destinationAirport', max_length=4, blank=True, null=True)  # Field name made lowercase.
    destinationairportid = models.CharField(db_column='destinationAirportId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stops = models.IntegerField(blank=True, null=True)
    equipment = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flightdata'
