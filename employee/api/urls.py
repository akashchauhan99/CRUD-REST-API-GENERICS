from django.urls import path
from .views import EmployeeDeleteView, EmployeePostView, EmployeeGetView, EmployeeUpdateView

urlpatterns = [
    # for post
    path('api/create/', EmployeePostView.as_view()),
    # for get
    path('api/', EmployeeGetView.as_view()),
    # for get,put, patch
    path('api/update/<int:pk>/', EmployeeUpdateView.as_view()),
    # for delete
    path('api/delete/<int:pk>/', EmployeeDeleteView.as_view()),
]
