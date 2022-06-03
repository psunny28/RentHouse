from django.urls import path
from .import views

urlpatterns = [
    path('', views.agents, name='agents'),
    path('single_agent/<int:agent_id>/', views.single_agent, name='single_agent'),
]
