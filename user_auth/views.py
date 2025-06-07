from django.shortcuts import render
from .models import Profile
from rest_framework import status
from .serializers import ProfileSerializer,UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics, permissions
# Create your views here.
class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            print("user=",user)
            return Response({"message": "User created successfully","id":user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['exam_name', 'batch']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProfileRetrieveUpdateDelete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        print("user=",self.request.user)
        print("dfg=",Profile.objects.get(user=self.request.user))
        return Profile.objects.get(user=self.request.user)
