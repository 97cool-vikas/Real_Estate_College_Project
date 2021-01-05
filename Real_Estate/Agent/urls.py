from django.contrib import admin
from django.urls import path
from . import views


app_name = "agent"

urlpatterns = [
    path('index.html/', views.AgentListView.as_view(), name='list'),
    path('index.html/', views.agent_page, name='agent_page'),
    path('detail/<int:pk>/', views.AgentDetailView.as_view(), name='detail'),
    path('register.html', views.AgentCreateView.as_view(), name='create'),
    path('create/success.html', views.success_agent_create, name='success_create'),

    path('update/<int:pk>/', views.AgentUpdateView.as_view(), name='update'),
]