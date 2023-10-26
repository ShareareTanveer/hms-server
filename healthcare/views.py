from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from permisions.permissions import IsAdminAndHROrReadOnly, IsAdminAndReceptionistOrNothing, IsAdminAndHROrDoctor, IsAdminAndReceptionistOrPatient, IsAdminAndReceptionistOrPatientReadOnly
from core.models import Employee, UserDetail
from .paginations import StandardResultsSetPagination
from .models import Day, Department, Doctor, Patient, Schedule, Appointment, Bed, BedAssign, BirthReport, DeathReport
from .serializers import CountSerializer, DashboardAppointmentSerializer, DaySerializer, DepartmentSerializer, DoctorAvailableDaySerializer, DoctorAvailableTimeSlotSerializer, DoctorSceduleByIdSerializer, DoctorSerializer, GetBedAssignSerializer, GetDashboardAppointmentSerializer, GetDoctorSerializer, GetScheduleSerializer, PatchDashboardAppointmentSerializer, PatchScheduleSerializer, PostDoctorSerializer, ScheduleSerializer, AppointmentSerializer, BedSerializer, BedAssignSerializer, BirthReportSerializer, DeathReportSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminAndHROrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter]
    search_fields = ['id', 'name', 'description']
    ordering_fields = ['name', 'status', 'id']


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminAndHROrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter]
    search_fields = ['id', 'user_details_id__user_id__email',
                     'user_details_id__user_id__first_name']
    ordering_fields = ['id', 'status']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetDoctorSerializer    
        elif self.request.method == 'POST':
            return PostDoctorSerializer
        return DoctorSerializer    


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter]
    search_fields = ['id', 'doctor',
                     'available_days']
    ordering_fields = ['id','doctor', 'status']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetScheduleSerializer    
        elif self.request.method == 'PATCH':
            return PatchScheduleSerializer
        return ScheduleSerializer
    
    @action(detail=False, methods=['POST'])
    def doctorbyid(self, request):

        if request.method == 'POST':
            serializer = DoctorSceduleByIdSerializer(data=request.data)
            if serializer.is_valid():
                doctor_identifier = serializer.validated_data['doctor_id']
                doctor = None
                print(doctor_identifier)
                try:
                    doctor = Doctor.objects.get(id=doctor_identifier)
                except (Doctor.DoesNotExist, ValueError):
                    doctor = get_object_or_404(Doctor, user_details__user__email=doctor_identifier)
                schedule = get_object_or_404(Schedule, doctor=doctor)
                schedule_serializer = GetScheduleSerializer(schedule)  # Serialize the Schedule instance
                return Response({'schedule':schedule_serializer.data }, status=status.HTTP_200_OK)

  
    @action(detail=False, methods=['POST'])
    def available(self, request):

        if request.method == 'POST':
            serializer = DoctorAvailableTimeSlotSerializer(data=request.data)

            if serializer.is_valid():
                doctor_identifier = serializer.validated_data['doctor']
                appointment_date = serializer.validated_data['appointment_date']
                doctor = None

                try:
                    doctor = Doctor.objects.get(id=doctor_identifier)
                except (Doctor.DoesNotExist, ValueError):
                    doctor = get_object_or_404(Doctor, user_details__user__email=doctor_identifier)

                schedule = get_object_or_404(Schedule,doctor=doctor)
                all_time_slots = schedule.get_time_slots()
                booked_appointment = Appointment.objects.filter(
                    appointment_date=appointment_date, doctor=doctor)
                
                if(not booked_appointment.exists()):
                    response_data = {
                    'available_time_slots': all_time_slots,
                }
                    return Response(response_data, status=status.HTTP_201_CREATED)
                
                bookoed_time_slot = [timeslot.time_alloted.strftime(
                    "%H:%M") for timeslot in booked_appointment]
                available = [
                    item for item in all_time_slots if item not in bookoed_time_slot]

                response_data = {
                    'available_time_slots': available,
                }

                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['POST'])
    def day(self, request):
        if request.method == 'POST':
            serializer = DoctorAvailableDaySerializer(data=request.data)
            if serializer.is_valid():
                doctor = serializer.validated_data['doctor']
                day = get_object_or_404(Schedule,doctor=doctor)
                result= [d.name for d in day.available_days.all()]   
                return Response({'day':result}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = []



class DashboardAppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    # serializer_class = DashboardAppointmentSerializer
    permission_classes = [IsAdminAndReceptionistOrPatient]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetDashboardAppointmentSerializer    
        elif self.request.method == 'PATCH':
            return PatchDashboardAppointmentSerializer
        return DashboardAppointmentSerializer   
    
    def get_queryset(self):
        queryset = Appointment.objects.all()  # Default queryset
        
        if self.request.user.is_authenticated:  # Check if user is authenticated
            user_details = get_object_or_404(UserDetail, user__email=self.request.user)
     
            if user_details.user.role == 'PATIENT':
                patient= get_object_or_404(Patient, user_details=user_details)
                queryset = Appointment.objects.filter(patient=patient)           
            elif user_details.user.role == 'DOCTOR':
                doctor= get_object_or_404(Doctor, user_details=user_details)
                queryset = Appointment.objects.filter(doctor=doctor)
        return queryset

     


class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    permission_classes = [IsAdminAndReceptionistOrNothing]

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = []


class BedAssignViewSet(viewsets.ModelViewSet):
    queryset = BedAssign.objects.all()
    serializer_class = BedAssignSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminAndReceptionistOrPatientReadOnly]
    filter_backends = [filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter]
    search_fields = ['id', 'patient', 'bed']
    ordering_fields = ['id', 'patient', 'bed']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetBedAssignSerializer    
        # elif self.request.method == 'PATCH':
        #     return PatchScheduleSerializer
        return BedAssignSerializer    
    
    def get_queryset(self):
        queryset = BedAssign.objects.all()  # Default queryset
        
        if self.request.user.is_authenticated:  # Check if user is authenticated
            user_details = get_object_or_404(UserDetail, user__email=self.request.user)
     
            if user_details.user.role == 'PATIENT':
                patient= get_object_or_404(Patient, user_details=user_details)
                queryset = BedAssign.objects.filter(patient=patient)           
        return queryset


class BirthReportViewSet(viewsets.ModelViewSet):
    queryset = BirthReport.objects.all()
    serializer_class = BirthReportSerializer
    permission_classes = [IsAdminAndReceptionistOrNothing]


class DeathReportViewSet(viewsets.ModelViewSet):
    queryset = DeathReport.objects.all()
    serializer_class = DeathReportSerializer
    permission_classes = [IsAdminAndReceptionistOrNothing]



class CountSummaryView(APIView):
    def get(self, request, *args, **kwargs):
        doctors_count = Doctor.objects.filter(status=True).count()
        patients_count = Patient.objects.filter(status=True).count()
        employees_count = Employee.objects.filter(status=True).count()
        appointments_count = Appointment.objects.filter().count()

        data = {
            'doctors_count': doctors_count,
            'patients_count': patients_count,
            'employees_count': employees_count,
            'appointments_count': appointments_count,
        }

        serializer = CountSerializer(data)
        return Response(serializer.data)