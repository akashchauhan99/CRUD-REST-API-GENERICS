from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from ..models import Employee

# CreateAPIView - It is only use for post
class EmployeePostView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# ListAPIView - It is only use for get
class EmployeeGetView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# RetrieveUpdateAPIView - It is only use for get, put, patch
class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# DestroyAPIView - It is only user for delete
class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer