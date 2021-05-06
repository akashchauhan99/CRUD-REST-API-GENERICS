from .serializers import *

from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class CreateBlogApiView(CreateAPIView):
    serializer_class =BlogSerailzer2

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'created'},status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CreateApiViewApi(APIView):

    def post(self, request):
        serializer = BlogSerailzer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'crated successfully'},status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class BlogList(ListAPIView):
    queryset = Blog.objects.all()

    def get(self, request):
        qs = self.get_queryset()
        data = BlogSerializer(qs, many=True).data
        return Response({'data':data,'message':'blog list'},status=HTTP_200_OK)
