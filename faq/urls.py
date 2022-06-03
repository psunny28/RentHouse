from django.urls import path
from .import views

urlpatterns = [
    path("frequently-asked-questions/", views.faq, name='faq'),
]
