from django.shortcuts import get_object_or_404
from rest_framework import viewsets,status
from healthcare.models import Patient
from permisions.permissions import IsAdminAndReceptionistOrPatient
from healthcare.paginations import StandardResultsSetPagination
from core.models import UserDetail
from .models import PatientDocument, PatientCseStudy
from .serializers import PatientSerializer, PatientDocumentSerializer, PatientCseStudySerializer, PatientUserSerializer, PostPatientSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

class PatientViewSet(viewsets.ModelViewSet):
    # queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsAdminAndReceptionistOrPatient]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter]
    search_fields = ['id','user_details_id__user_id__email','user_details_id__user_id__first_name']
    ordering_fields = ['id','status']

    
    def get_serializer_class(self):  
        if self.request.method == 'POST':
            return PostPatientSerializer
        return PatientSerializer


    def get_queryset(self):
        queryset = Patient.objects.all()
        
        if self.request.user.is_authenticated:
            user_detail = get_object_or_404(UserDetail, user__email=self.request.user)
            
            if user_detail.user.role == 'PATIENT':
                queryset = Patient.objects.filter(user_details=user_detail)

        return queryset
    
    @action(detail=False, methods=['POST'])
    def user(self, request):
        if request.method == 'POST':
            serializer = PatientUserSerializer(data=request.data)
            if serializer.is_valid():
                user_id = serializer.validated_data['user_id']
                patient = get_object_or_404(Patient, user_details__user_id=user_id)
                print(patient.user_details.user.email)     
                return Response({'patient_id':patient.id,'email':patient.user_details.user.email}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PatientDocumentViewSet(viewsets.ModelViewSet):
    queryset = PatientDocument.objects.all()
    serializer_class = PatientDocumentSerializer
    permission_classes = [IsAdminAndReceptionistOrPatient]

    def get_queryset(self):
        if (self.request.user.role == 'PATIENT'):
            queryset = Patient.objects.filter(
                user_details__user_id=self.request.user.id)
        else:
            queryset = Patient.objects.all()
        return queryset
    



class PatientCseStudyViewSet(viewsets.ModelViewSet):
    queryset = PatientCseStudy.objects.all()
    serializer_class = PatientCseStudySerializer
    permission_classes = [IsAdminAndReceptionistOrPatient]

    def get_queryset(self):
        if (self.request.user.role == 'PATIENT'):
            queryset = Patient.objects.filter(
                user_details__user_id=self.request.user.id)
        else:
            queryset = Patient.objects.all()
        return queryset
