import datetime
from django.contrib.auth.models import User
from django.db import models

class CustomerDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Details"


class Payment(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    card_expiry = models.DateField(default=datetime.date.today)
    card_cvv = models.CharField(max_length=4, default='')

    def __str__(self):
        return f"Payment info for {self.user.username}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField(default=datetime.date.today)
    check_out_date = models.DateField(default=datetime.date.today)
    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE_CHOICES, default='single')
    num_guests = models.IntegerField(default=1)
    special_requests = models.TextField(default='No special requests')
    
    def __str__(self):
        return f"Reservation for {self.user.username}"

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comments = models.TextField(default='No comments')

    def __str__(self):
        return f"Feedback for {self.user.username}"
