from django.shortcuts import render

def services(request):
    return render(request, 'event_services/services.html')
