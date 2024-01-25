from django.contrib import admin
from .models import Reservation, Payment, Feedback, CustomerDetail

admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Feedback)
admin.site.register(CustomerDetail)