from datetime import date
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Payment, Reservation, Feedback, CustomerDetail

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'card_expiry', 'card_cvv']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in_date', 'check_out_date', 'room_type', 'num_guests', 'special_requests']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comments']

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetail
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'email']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']