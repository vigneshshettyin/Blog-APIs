import http
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework.authtoken.models import Token

# Create your views here.
class RegisterAPIView(APIView):

    """
    End-point for creating a new user.
    """
    serializer_class = UserRegisterSerializer

    def get_tokens_for_user(self, user):
        token = Token.objects.create(user=user)

        return {
            'token': str(token.key),
        }

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = self.get_tokens_for_user(user)
            return Response(response_data, status=http.HTTPStatus.CREATED)
        return Response(serializer.errors, status=http.HTTPStatus.BAD_REQUEST)