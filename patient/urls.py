from rest_framework import routers
from .views import PatientViewSet, PatientDocumentViewSet, PatientCseStudyViewSet



router = routers.DefaultRouter()
router.register('patients', PatientViewSet,basename='patient')
router.register('documents', PatientDocumentViewSet,basename='document')
router.register('case-studies', PatientCseStudyViewSet,basename='case-study')

urlpatterns = [
]

urlpatterns += router.urls