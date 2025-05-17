from django.urls import path
from .views import RegisterUserView, ProfileListCreate, ProfileRetrieveUpdateDelete
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', ProfileListCreate.as_view(), name='profile_list_create'),
    path('profile/<int:pk>/', ProfileRetrieveUpdateDelete.as_view(), name='profile_retrieve_update_delete'),
]