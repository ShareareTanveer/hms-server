from rest_framework import viewsets
from permisions.permissions import IsAdminAndAccountantAndReceptionistOrNothing,IsAdminAndReceptionistOrNothing
from .models import Account, Invoice, AccountPayment, Service, Package,Bill,PatientAdmission
from .serializers import AccountSerializer, InvoiceSerializer, AccountPaymentSerializer, ServiceSerializer, PackageSerializer,PatientAdmissionSerializer , BillSerializer
# Create your views here.


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes=[IsAdminAndAccountantAndReceptionistOrNothing]


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes=[IsAdminAndAccountantAndReceptionistOrNothing]


class AccountPaymentViewSet(viewsets.ModelViewSet):
    queryset = AccountPayment.objects.all()
    serializer_class = AccountPaymentSerializer
    permission_classes=[IsAdminAndAccountantAndReceptionistOrNothing]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes=[IsAdminAndAccountantAndReceptionistOrNothing]

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes=[IsAdminAndAccountantAndReceptionistOrNothing]

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes=[IsAdminAndAccountantAndReceptionistOrNothing]

class PatientAdmissionViewSet(viewsets.ModelViewSet):
    queryset = PatientAdmission.objects.all()
    serializer_class = PatientAdmissionSerializer
    permission_classes=[IsAdminAndReceptionistOrNothing]
