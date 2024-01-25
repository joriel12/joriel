from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import PaymentForm, ReservationForm, FeedbackForm, RegistrationForm, CustomerDetailsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .models import Reservation, CustomerDetail, Payment, Feedback

def home_view(request):
    return render(request, 'pages/home.html') 

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('customer_details')
    else:
        form = RegistrationForm()
    
    return render(request, 'pages/registration_form.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'pages/login.html', {'form': form})

def custom_logout(request):
    django_logout(request)
    return redirect('home')

#RESERVATION INFO
@login_required
def reservation_form_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Set the user to the currently logged-in user
            reservation.save()
            return redirect('home')
    else:
        form = ReservationForm()
    
    return render(request, 'pages/reservation_form.html', {'form': form})


@login_required
def view_reservations(request):
    user_reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'pages/view_reservations.html', {'user_reservations': user_reservations})

@login_required
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view_reservations')  # Redirect to view reservations after updating
    else:
        form = ReservationForm(instance=reservation)
    
    return render(request, 'pages/update_reservation.html', {'form': form})

@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)
    
    if request.method == 'POST':
        
        reservation.delete()
        return redirect('view_reservations')  # Redirect to view reservations after cancellation
    

    return redirect('view_reservations')




#PAYMENT INFO
@login_required
def payment_form_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            Payment = form.save(commit=False)
            Payment.user = request.user
            Payment.save()
            return redirect('home')
    else:
        form = PaymentForm()
    
    return render(request, 'pages/payment_form.html', {'form': form})

@login_required
def view_payments(request):
    user_payments = Payment.objects.filter(user=request.user)
    return render(request, 'pages/view_payments.html', {'user_payments': user_payments})

#CUSTOMER INFO
@login_required
def customer_details_view(request):
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            customer_details = form.save(commit=False)
            customer_details.user = request.user
            customer_details.save()
            return redirect('payment_form') 
    else:
        form = CustomerDetailsForm()
    
    return render(request, 'pages/customer_details.html', {'form': form})

@login_required
def view_CustomerDetails(request):
    user_CustomerDetails = CustomerDetail.objects.filter(user=request.user)
    return render(request, 'pages/view_customerDetails.html', {'user_CustomerDetails': user_CustomerDetails})

#FEEDBACK
def feedback_form_view(request):
    if not request.user.is_authenticated:

        return redirect('login')
    else:
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                Feedback = form.save(commit=False)
                Feedback.user = request.user
                Feedback.save()
                return redirect('view_feedback')
        else:
            form = FeedbackForm()

        return render(request, 'pages/feedback_form.html', {'form': form})




def view_feedback(request):
    view_feedback = Feedback.objects.all()
    return render(request, 'pages/view_feedback.html', {'view_feedback': view_feedback})


