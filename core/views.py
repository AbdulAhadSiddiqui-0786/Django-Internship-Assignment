from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.views import LoginView

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is a public endpoint and does not require authentication."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello {request.user.username}, you are authenticated."})



class UserLoginView(LoginView):
    template_name = 'login.html'
