from django.urls import path
from .views import gallery_view # type: ignore

urlpatterns = [
    path('', gallery_view, name='gallery'),
]


