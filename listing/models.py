from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Listing(models.Model):
    CHOICE_STATUS = (
        ('SL', 'Sale'),
        ('RN', 'Rent'),
        ('DN', 'Done'),
    )

    CHOICE_TYPE = (
        ('HS', 'House'),
        ('AP', 'Apartment')
    )

    address = models.CharField(max_length=100)
    about = models.TextField()

    type = models.CharField(
        max_length=2,
        choices=CHOICE_TYPE,
        default='HS'
    )

    status = models.CharField(
        max_length=2,
        choices=CHOICE_STATUS,
        default='SL'
    )
    number_of_rooms = models.IntegerField()
    price = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.address)


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)