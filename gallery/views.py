from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Save the form data to the database
            return redirect('contact_success')  # Redirect after submission
    else:
        form = ContactForm()
    
    return render(request, 'event_services/contact_us.html', {'form': form})
