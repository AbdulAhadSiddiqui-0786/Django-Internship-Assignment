from django.urls import path
from . import views

urlpatterns = [
    path('', public_view, name='home'),  # 👈 default homepage
    path('api/public/', public_view, name='public'),
    path('api/protected/', protected_view, name='protected'),
    path('login/', UserLoginView.as_view(), name='login'),  # for form login
]