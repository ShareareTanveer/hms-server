from rest_framework import serializers
from .models import Account, Invoice, AccountPayment, Service, Package, PatientAdmission, Bill


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name',
                  'account_type', 'description', 'status']


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'account', 'patient', 'doctor', 'quantity', 'date',
                  'price', 'vat', 'discount', 'grand_total', 'paid', 'due',
                  'updated_at', 'created_at',
                  'status']


class AccountPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountPayment
        fields = ['id', 'account', 'date', 'doctor', 'pay_to', 'description',
                  'amount', 'status']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_name', 'description',
                  'quantity', 'rate', 'status']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'package_name', 'description',
                  'service', 'discount', 'status']


class PatientAdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAdmission
        fields = ['id', 'admission_date', 'doctor',
                  'patient', 'discharge_date',
                  'package_name', 'insurance_name',
                  'policy_no', 'agent_name',
                  'guardian_name', 'guardian_relation',
                  'guardian_contact', 'guardian_address',
                  'status']
        
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'amount', 'admission', 'doctor', 'payment_method', 'service',
                  'date', 'vat_percent', 'discount_percent', 'paid_amount', 'due_amount', 'receipt_no',
                  'updated_at', 'created_at',
                  'status']
