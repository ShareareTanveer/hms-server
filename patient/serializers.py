from rest_framework import serializers
from core.models import UserDetail
from core.serializers import SimpleUserDetailSerializer
from healthcare.models import Patient
from .models import PatientDocument,PatientCseStudy
from django.contrib.auth import get_user_model

User = get_user_model()


class PatientUserSerializer(serializers.Serializer):
    user_id = serializers.CharField()

        
class PatientSerializer(serializers.ModelSerializer):
    user_details = SimpleUserDetailSerializer()
    patient_id = serializers.CharField(read_only=True)
    class Meta:
        model = Patient
        fields = ['id', 'patient_id', 'occupation', 'medical_history', 'status', 'user_details']
        
class PostPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'occupation', 'medical_history', 'status', 'user_details']

    # def create(self, validated_data):
    #     patient_data = validated_data.copy()
    #     user_details_data = patient_data.pop('user_details')
    #     user_data = user_details_data.pop('user')
    #     user = User.objects.create(**user_data, role='PATIENT')
    #     user_details = UserDetail.objects.create(user=user, **user_details_data)
    #     patient = self.Meta.model.objects.create(user_details=user_details, **patient_data)
    #     return patient


class PatientDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDocument
        fields = ['id', 'patient','doctor' 'prescription', 'medical_report', 'consent_form',
                  'created_at', 'updated_at']
        

class PatientCseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCseStudy
        fields = ['id', 'patient', 'food_allergies', 'tendency_bleed', 'heart_disease', 'high_blood_pressure',
                  'diabetic', 'surgery', 'accident', 'others', 'family_medical_history', 'current_medication',
                  'female_pregnancy', 'breast_feeding', 'health_insurance', 'low_income', 'reference',
                  'status']
