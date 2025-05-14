from django.urls import path
from .views import McqQuestionListCreate,McqRetrieveUpdateDelete,UniqueFieldApiView
urlpatterns = [
    path('mcq/',McqQuestionListCreate.as_view(),name="mcq_list_create" ),
    path('mcq/<int:pk>/',McqRetrieveUpdateDelete.as_view(),name="mcq_retrieve_update_delete" ),
    path('unique_fields/',UniqueFieldApiView.as_view(),name="unique_fields" ),
]
