from django.urls import path
from .views import McqQuestionListCreate,McqRetrieveUpdateDelete,UniqueFieldApiView,CourseListCreate,BatchListCreate,StudentExamRecordListCreate,UniqueTestName
urlpatterns = [
    path('mcq/',McqQuestionListCreate.as_view(),name="mcq_list_create" ),
    path('mcq/<int:pk>/',McqRetrieveUpdateDelete.as_view(),name="mcq_retrieve_update_delete" ),
    path('unique_fields/',UniqueFieldApiView.as_view(),name="unique_fields" ),
    path('course/',CourseListCreate.as_view(),name="course_list_create" ),
    path('batch/',BatchListCreate.as_view(),name="batch_list_create" ),
    path('student_exam_record/',StudentExamRecordListCreate.as_view(),name="student_exam_record_list_create" ),
    path('unique_test_name/', UniqueTestName.as_view(), name="unique_test_name" ),

]
