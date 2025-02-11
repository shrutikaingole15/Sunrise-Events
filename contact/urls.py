from django.urls import path
from .views import contact_page  # ✅ Ensure this matches views.py

urlpatterns = [
    path('', contact_page, name='contact'),  # ✅ URL name must be 'contact'
]
