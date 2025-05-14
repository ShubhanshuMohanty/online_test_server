from django.shortcuts import render
from .serializers import McqQuestionSerializer
from .models import McqQuestion
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

# Create your views here.

#List & Create API View
class McqQuestionListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = McqQuestion.objects.all()
    serializer_class = McqQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exam_name', 'batch']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class McqRetrieveUpdateDelete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=McqQuestion.objects.all()
    serializer_class=McqQuestionSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class UniqueFieldApiView(APIView):
    def get(self,request):
        exam_name=McqQuestion.objects.values_list('exam_name',flat=True).distinct()
        batch=McqQuestion.objects.values_list('batch',flat=True).distinct()
        print("exam name=",list(exam_name))
        return Response({
            'exam_name':list(exam_name),
            'batch':list(batch)
        })
