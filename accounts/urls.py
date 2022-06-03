from django.urls import path
from .import views
from listings.models import Listing

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('bookmark_properties/', views.bookmark_properties, name='bookmark_properties'),
    path('my_property/', views.my_property, name='my_property'),
    # account verification
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('ResetPassword/', views.ResetPassword, name='ResetPassword'),
]
