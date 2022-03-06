from django.urls import reverse 
from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class DogsList(generics.ListCreateAPIView):
    # def get(self, request, format=None):
    #     dogs = DogSerializer(dogs, many=True)
    #     return Response(serializers.data)
        
    # def post(self, request, serializer):
    #     serializer = DogSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class BreedsList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = 'breed'

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class ApiRoot(generics.GenericAPIView):
    name = 'Dog API'
    def get(self, request, *args, **kwargs):
        return Response({
            'dogs': reverse(DogsList.name, request=request),
            'breeds': reverse(BreedsList.name, request=request),
            
        })