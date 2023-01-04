from rest_framework import generics 
from .serializers import UserSerializer, GameSerializer, ReviewSerializer
from .models import User, Game, Review
from rest_framework.response import Response

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameUpdate(generics.RetrieveUpdateDestroyAPIView):
    def put(self,request,pk):
        try:
            gameObj=Game.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeobj=GameSerializer(gameObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class ReviewPost(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request):
        reviewObj=Review.objects.all()
        reviewSerializeObj=ReviewSerializer(reviewObj,many=True)
        return Response(reviewSerializeObj.data)
    
    def post(self,request):
        serializeobj=ReviewSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class ReviewUpdate(generics.RetrieveUpdateDestroyAPIView):
    def put(self,request,pk):
        try:
            reviewObj=Review.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeobj=ReviewSerializer(reviewObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class ReviewDelete(generics.RetrieveUpdateDestroyAPIView):
    def delete(self,request,pk):
        try:
            reviewObj=Review.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        reviewObj.delete()
        return Response(200)

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer