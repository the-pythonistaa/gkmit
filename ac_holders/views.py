from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account
from .serializers import DepositeSerializer


# Create your views here.
class AccountViews(APIView):

    def post(self, request):
        return Response({'Hello': 'POST'}, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response({'Hello': 'DELETE'}, status=status.HTTP_200_OK)

    def get(self, request):
        print("HHHHHHHHHHHHHH===============")
        queryset = Account.objects.all()
        serializer_class = DepositeSerializer
        # return Response(serializer_class.data, status=status.HTTP_200_OK)
