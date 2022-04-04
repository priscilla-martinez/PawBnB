from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers.home import HomeSerializer 
from ..models.home import Home


class HomesView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        homes = Home.objects
        data = HomeSerializer(homes, many=True).data
        return Response(data)


class HomeView(APIView):
    def get(self, request, pk):
        home = get_object_or_404(Home, pk=pk)
        data = HomeSerializer(home).data
        return Response(data)
    
    def delete(self, request, pk):
        home = get_object_or_404(Home, pk=pk)
        home.delete()
        return Response( {'msg': 'Home has been deleted'} , status=status.HTTP_204_NO_CONTENT )

    def put(self, request, pk): 
        home = get_object_or_404(Home, pk=pk)
        request.data['owner'] = request.user.id
        updated_home = HomeSerializer(home, data=request.data)
        if updated_home.is_valid(): 
            updated_home.save()
            return Response(updated_home.data)
        else: 
            return Response(updated_home.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        request.data['owner'] = request.user.id
        home = HomeSerializer(data=request.data)
        if home.is_valid():
            home.save()
            return Response(home.data, status=status.HTTP_201_CREATED)
        else:
            return Response(home.errors, status=status.HTTP_400_BAD_REQUEST)

