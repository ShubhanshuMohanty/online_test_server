from django.utils import timezone
from django.shortcuts import render
from .serializers import McqQuestionSerializer, CourseSerializer, BatchSerializer,StudentExamRecordSerializer, TestSerializer
from .models import McqQuestion, Course, Batch , StudentExamRecord,Test
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404,ListAPIView
from rest_framework.exceptions import NotFound
from user_auth.models import Profile
from .filters import McqQuestionFilter

# Create your views here.

#List & Create API View
class McqQuestionListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = McqQuestion.objects.all()
    serializer_class = McqQuestionSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['exam_name', 'batch', 'test_name']
    filterset_class = McqQuestionFilter

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

# list & create API view for Course
class CourseListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BatchListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class StudentExamRecordListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = StudentExamRecord.objects.all()
    serializer_class = StudentExamRecordSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UniqueTestName(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        # print("request user =", request.user)
        test_names = McqQuestion.objects.values_list('test_name', flat=True).distinct()
        return Response(test_names)
    # {'test_names': list(test_names)}


#unoptimised code for test data details
'''
class TestDataDetails(ListAPIView):
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print("request user =", user)
        try:
            batch = Profile.objects.get(user=user).batch
            incomplete_test_ids = StudentExamRecord.objects.filter(
                student=user,
                is_completed=False
            )#.values_list('exam', flat=True)
            incomple_exam_name=[record.exam.name for record in incomplete_test_ids]
            print("incomplete exam names =", incomple_exam_name)
            
            print("user batch =", batch)
            ts=Test.objects.filter(batch=batch)
            matching_tests = []
            for test in ts:
                print("test name =", str(test.name))
                if str(test.name) in incomple_exam_name:
                    matching_tests.append(test)
                print("matching tests =", test)
            print("matching tests =", matching_tests)
            print("ts =", ts)
            return matching_tests
            # return Test.objects.filter(batch=batch)
        except Profile.DoesNotExist:
            raise NotFound(detail="Profile not found for this user.")
'''

#optimize code for test data details
# '''
class TestDataDetails(ListAPIView):
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print("Request user:", user)

        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise NotFound(detail="Profile not found for this user.")

        batch = profile.batch
        print("User batch:", batch)

        # Get names of incomplete exams
        incomplete_records = StudentExamRecord.objects.filter(student=user, is_completed=False)
        incomplete_exam_names = incomplete_records.values_list('exam__name', flat=True)

        print("Incomplete exam names:", list(incomplete_exam_names))

        # Filter tests by batch and name match
        matching_tests = Test.objects.filter(batch=batch, name__in=incomplete_exam_names)

        print("Matching tests:", list(matching_tests))
        return matching_tests
# '''

# update
class StudentExamRecordViewSet(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def patch(self,request,exam_id):
        student=request.user
        exam=exam_id
        score=request.data.get('score', None)
        print(f"student={student}, exam={exam} score={score}")
        try:
            exam = Test.objects.get(name=exam_id)
        except Exception:
            pass
        try:
            record = StudentExamRecord.objects.get(student=student, exam=exam)
            record.is_completed = True
            record.score = score
            record.completed_at = timezone.now()
            record.save()
            return Response({"message": "Exam record updated successfully."})
        except StudentExamRecord.DoesNotExist:
            return Response({"error": "Exam record not found."}, status=404)