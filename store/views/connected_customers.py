from django.shortcuts import render
from .models import customer  # Import your Customer model

def schedule_meeting(request):
    connected_customers = customer.objects.all()  # Fetch all customers (adjust as needed)
    return render(request, 'schedule_meeting.html', {'connected_customers': connected_customers})
