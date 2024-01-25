from django.urls import path
from . import views
from .views import custom_logout

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    
    path('customer-details/', views.customer_details_view, name='customer_details'),
    path('payment-form/', views.payment_form_view, name='payment_form'),
    path('view-payments/',views.view_payments, name='view_payments'),
    path('reservation-form/', views.reservation_form_view, name='reservation_form'),
    path('feedback-form/', views.feedback_form_view, name='feedback_form'),
    path('view-feedback/',views.view_feedback, name='view_feedback'),
    path('logout/', custom_logout, name='custom_logout'),
    path('view-reservations/', views.view_reservations, name='view_reservations'),
    path('view-CustomerDetails/',views.view_CustomerDetails, name='view_CustomerDetails'),
    path('update-reservation/<int:reservation_id>/', views.update_reservation, name='update_reservation'),
    path('cancel_reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation')
]
