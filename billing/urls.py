from rest_framework import routers
from .views import AccountViewSet, InvoiceViewSet,AccountPaymentViewSet, ServiceViewSet, PackageViewSet,BillViewSet, PatientAdmissionViewSet



router = routers.DefaultRouter()
router.register('accounts', AccountViewSet,basename='account')
router.register('invoices', InvoiceViewSet,basename='invoice')
router.register('account-payments', AccountPaymentViewSet,basename='account-payment')
router.register('services', ServiceViewSet,basename='service')
router.register('packages', PackageViewSet,basename='package')
router.register('patient-admissions', PatientAdmissionViewSet,basename='patient-admission')
router.register('bills', BillViewSet,basename='bill')

urlpatterns = [
]

urlpatterns += router.urls