import datetime
from rest_framework import serializers
from core.models import UserDetail
from core.serializers import SimpleUserDetailSerializer
from patient.serializers import PatientSerializer
from .models import Day, Department, Doctor, Schedule, Appointment, Bed, BedAssign, BirthReport,DeathReport
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()



class DoctorAvailableTimeSlotSerializer(serializers.Serializer):
    doctor=serializers.CharField()
    appointment_date=serializers.CharField()
    

class DoctorAvailableDaySerializer(serializers.Serializer):
    doctor=serializers.CharField()



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'status']


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'name']


class GetDoctorSerializer(serializers.ModelSerializer):
    user_details = SimpleUserDetailSerializer()
    department = serializers.StringRelatedField(source='department.name')  # Use 'name' attribute of the related department
    class Meta:
        model = Doctor
        fields = ['id', 'designation', 'department', 'short_bio', 'spacialist',
                  'education_degree', 'status', 'visiting_fee', 'user_details']

class DoctorSceduleByIdSerializer(serializers.Serializer):
    doctor_id = serializers.CharField()


class PostDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'designation', 'department', 'short_bio', 'spacialist',
                  'education_degree', 'status', 'visiting_fee', 'user_details']

class DoctorSerializer(serializers.ModelSerializer):
    user_details = SimpleUserDetailSerializer()
    class Meta:
        model = Doctor
        fields = ['id', 'designation', 'department', 'short_bio', 'spacialist',
                  'education_degree', 'status', 'visiting_fee', 'user_details']

    # def create(self, validated_data):
    #     doctor_data = validated_data.copy()
    #     user_details_data = doctor_data.pop('user_details')
    #     user_data = user_details_data.pop('user')
    #     user = User.objects.create(**user_data, role='DOCTOR')
    #     user_details = UserDetail.objects.create(
    #         user=user, **user_details_data)
    #     doctor = Doctor.objects.create(
    #         user_details=user_details, **doctor_data)
    #     return doctor


class ScheduleSerializer(serializers.ModelSerializer):
    available_time_slots = serializers.SerializerMethodField(read_only=True,method_name='get_available_time_slots')
    # doctor=serializers.StringRelatedField()
    # available_days=serializers.StringRelatedField(many=True)
    class Meta:
        model = Schedule
        fields = ['id', 'doctor', 'start_time', 'end_time', 'per_patient_time',
                  'available_days', 'status','available_time_slots']
        
    def get_available_time_slots(self,obj):
        return obj.get_time_slots()
    
class GetScheduleSerializer(serializers.ModelSerializer):
    doctor=serializers.StringRelatedField()
    available_days=serializers.StringRelatedField(many=True)
    class Meta:
        model = Schedule
        fields = ['id', 'doctor', 'start_time', 'end_time', 'per_patient_time',
                  'available_days', 'status']
        
class PatchScheduleSerializer(serializers.ModelSerializer):
    # available_days=serializers.StringRelatedField()
    class Meta:
        model = Schedule
        fields = ['id', 'start_time', 'end_time', 'per_patient_time',
                  'available_days', 'status']
        
    def get_available_time_slots(self,obj):
        return obj.get_time_slots()
        


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'appointment_date', 'department',
                  'time_alloted', 'problem','patient','serial_no']
        
                
    def validate(self, attrs):
        doctor = attrs['doctor']
        appointment_date = attrs['appointment_date']
        time_alloted = attrs['time_alloted']
        schedule=get_object_or_404(Schedule, doctor=doctor)
        doctor_available_on = [i.name.lower() for i in schedule.available_days.all()]

        start_time=schedule.start_time
        end_time=schedule.end_time

        # chexk if time_alloted already exists in appointment_date
        exists_time_alloted = Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date,time_alloted=time_alloted).first()
        if exists_time_alloted:
            raise serializers.ValidationError("Doctor is not available at the requested time Slot.")

         # Check if doctor is available on the requested Time
        if time_alloted <= start_time or time_alloted >= end_time:
            raise serializers.ValidationError("Doctor is not available at the requested time.")

         # Check if doctor is available on the requested day
        if not appointment_date.strftime('%A').lower() in doctor_available_on:
            raise serializers.ValidationError("Doctor is not available at the requested appointment time.")

        return attrs
    
    # def create(self, validated_data):
    #     patient_data = validated_data.pop('patient')
    #     patient_serializer = PatientSerializer(data=patient_data)
    #     patient_serializer.is_valid(raise_exception=True)
    #     patient = patient_serializer.save()

    #     appointment = Appointment.objects.create(patient=patient, **validated_data)
    #     return appointment
        

class GetDashboardAppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'appointment_date', 'department',
                  'time_alloted', 'problem','patient','serial_no']


class PatchDashboardAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'appointment_date', 'department',
                  'time_alloted', 'problem','patient','serial_no']
        
class DashboardAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'appointment_date', 'department',
                  'time_alloted', 'problem','patient','serial_no']
        
                
    def validate(self, attrs):
        doctor = attrs['doctor']
        appointment_date = attrs['appointment_date']
        time_alloted = attrs['time_alloted']
        schedule=get_object_or_404(Schedule, doctor=doctor)
        doctor_available_on = [i.name.lower() for i in schedule.available_days.all()]

        start_time=schedule.start_time
        end_time=schedule.end_time

        # chexk if time_alloted already exists in appointment_date
        exists_time_alloted = Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date,time_alloted=time_alloted).first()
        if exists_time_alloted:
            raise serializers.ValidationError("Doctor is not available at the requested time Slot.")

         # Check if doctor is available on the requested Time
        if time_alloted <= start_time or time_alloted >= end_time:
            raise serializers.ValidationError("Doctor is not available at the requested time.")

         # Check if doctor is available on the requested day
        if not appointment_date.strftime('%A').lower() in doctor_available_on:
            raise serializers.ValidationError("Doctor is not available at the requested appointment time.")

        return attrs
        


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = ['id', 'bed_type', 'description', 'bed_capacity', 'charge',
                  'status']


class GetBedAssignSerializer(serializers.ModelSerializer):
    patient = serializers.StringRelatedField()
    bed = serializers.StringRelatedField()
    
    class Meta:
        model = BedAssign
        fields = ['id', 'bed', 'patient', 'description', 'assigned_date', 'discharge_date', 'status']

class BedAssignSerializer(serializers.ModelSerializer):
    # patient = serializers.StringRelatedField()
    
    class Meta:
        model = BedAssign
        fields = ['id', 'bed', 'patient', 'description', 'assigned_date', 'discharge_date', 'status']
                             
    def validate(self, attrs):
        bed = attrs.get('bed')
        if bed is None:
            raise serializers.ValidationError("The 'bed' field is required.")

        date = attrs.get('discharge_date')
        if date is None:
            raise serializers.ValidationError("The 'discharge_date' field is required.")

        is_bed_available = bed.is_available()

        if is_bed_available:
            return attrs
        else:
            raise serializers.ValidationError("The bed is not available.")

class BirthReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirthReport
        fields = ['id', 'patient', 'place_of_birth', 'description', 'weight', 'delivery_type', 'created_at', 'updated_at']
        
class DeathReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeathReport
        fields = ['id', 'patient', 'place_of_death', 'description', 'cause_of_death', 'created_at', 'updated_at']

class CountSerializer(serializers.Serializer):
    doctors_count = serializers.IntegerField()
    patients_count = serializers.IntegerField()
    employees_count = serializers.IntegerField()
    appointments_count = serializers.IntegerField()