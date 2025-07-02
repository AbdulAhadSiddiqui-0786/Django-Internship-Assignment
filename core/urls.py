from django.urls import path
from . import views

urlpatterns = [
    path('public/', views.public_view),
    path('protected/', views.protected_view),
    path('login/', views.UserLoginView.as_view(), name='login'),
]
