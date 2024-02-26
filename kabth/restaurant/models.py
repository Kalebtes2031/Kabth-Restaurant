from django.db import models
import datetime

class Menu(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Booking(models.Model):
    firstName = models.CharField(max_length = 250)
    lastName = models.CharField(max_length=250)
    guestNumber = models.IntegerField()
    preferredDate = models.DateField(default=datetime.date.today)
    preferredTime = models.TimeField(default=datetime.time(12, 0))
    specialRequests = models.TextField(blank = True, null= True)

    def __str__(self):
        return self.firstName + " " + self.lastName