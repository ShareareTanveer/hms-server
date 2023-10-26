from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from permisions.permissions import IsAdminAndHROrReadOnly, IsAdminAndHROrNothing, IsAdminOrReadOnly
from .models import Employee, Notice, AppSettings, UserDetail
from .serializers import EmployeeSerializer, NoticeSerializer, AppSettingsSerializer, PostUserDetailSerializer, UserDetailByUserIdSerializer, UserDetailSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth import get_user_model

from django.apps import apps
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import action

User = get_user_model()

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminAndHROrReadOnly]


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAdminAndHROrNothing]


class AppSettingsViewSet(viewsets.ModelViewSet):
    queryset = AppSettings.objects.all()
    serializer_class = AppSettingsSerializer
    permission_classes = [IsAdminOrReadOnly]


class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    # permission_classes = [IsAdminOrReadOnly]


 
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostUserDetailSerializer
        return UserDetailSerializer

    @action(detail=False, methods=['POST'])
    def user(self, request):
        if request.method == 'POST':
            serializer = UserDetailByUserIdSerializer(data=request.data)
            if serializer.is_valid():
                user_id = serializer.validated_data['user_id']
                user_details = get_object_or_404(UserDetail, user=user_id)
                serializer = UserDetailSerializer(user_details)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BulkDeleteAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request):
        app_name = request.data.get('app_name')
        model_name = request.data.get('model_name')
        selected_rows = request.data.get('selected_rows')

        if not app_name:
            return Response({'error': 'App name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if not model_name:
            return Response({'error': 'Model name is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            model = apps.get_model(app_label=app_name, model_name=model_name)
        except LookupError:
            return Response({'error': f'Model "{model_name}" not found in app "{app_name}".'}, status=status.HTTP_404_NOT_FOUND)

        if not selected_rows:
            return Response({'error': 'No rows selected for deletion.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Delete the selected rows
            model.objects.filter(id__in=selected_rows).delete()

            return Response({'message': f'Bulk delete on "{model_name}" performed successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
