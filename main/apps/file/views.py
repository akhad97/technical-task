from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import File, FileGroup
from .serializer import FileCreateSerializer, FileLitSerializer, FileGroupSerializer
from .permission import CanReadPermission, CanChangePermission
from rest_framework.response import Response
from rest_framework import status



class FileListCreate(generics.ListCreateAPIView):
    queryset = File.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FileCreateSerializer
        else:
            return FileLitSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

file_list_create_api_view = FileListCreate.as_view()


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileLitSerializer
    permission_classes = [CanReadPermission, CanChangePermission]

file_api_view = FileDetail.as_view()


class FileShare(generics.UpdateAPIView):
    queryset = File.objects.all()
    serializer_class = FileLitSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        shared_users = request.data.get('shared_with', [])        
        instance.shared_with.clear()
        for user_id in shared_users:
            instance.shared_with.add(user_id)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

file_share_api_view = FileShare.as_view()


class FileGroupCreateAPIView(generics.ListCreateAPIView):
    queryset = FileGroup.objects.all()
    serializer_class = FileGroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

filegroup_list_create_api_view = FileGroupCreateAPIView.as_view()


class FileGroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FileGroup.objects.all()
    serializer_class = FileGroupSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='id'

filegroup_api_view = FileGroupDetailAPIView.as_view()