from django.db import models

class DevicesModel(models.Model):
    governorate = models.CharField(max_length = 255, blank=True, null=True)
    sector = models.CharField(max_length = 255, blank=True, null=True)
    office = models.CharField(max_length = 255, blank=True, null=True)
    officeType = models.CharField(max_length = 255, blank=True, null=True)
    model = models.CharField(max_length = 255, blank=True, null=True)
    serial = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255, blank=True, null=True)
    status = models.CharField(max_length = 255, blank=True, null=True)
    ram = models.CharField(max_length = 255, blank=True, null=True)
    deviceType = models.CharField(max_length = 255, blank=True, null=True)
    sectorCode = models.CharField(max_length = 255, blank=True, null=True)
    numOfWindows = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length = 255, blank=True, null=True)
    
class OfficesModel(models.Model):
    sector = models.CharField(max_length = 255)
    sectorCode = models.IntegerField()
    office = models.CharField(max_length = 255)
    officeType = models.CharField(max_length = 255)
    numOfWindows = models.IntegerField()

class SectorModel(models.Model):
    governorate = models.CharField(max_length = 255)
    sectorCode = models.IntegerField()
    sector = models.CharField(max_length = 255)


class DevicesModuleModel(models.Model):
    model = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)
    status = models.CharField(max_length = 255)
    ram = models.CharField(max_length = 255)
    deviceType = models.CharField(max_length = 255)
    serial = models.CharField(max_length = 255)
