from django.urls import path
from rest_framework import routers

from .views import BulkDeleteAPIView, EmployeeViewSet, NoticeViewSet, AppSettingsViewSet, UserDetailViewSet


router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')
router.register('notices', NoticeViewSet, basename='notice')
router.register('app-settings', AppSettingsViewSet, basename='app-setting')
router.register('user-details', UserDetailViewSet, basename='user-detail')

urlpatterns = [
    path('bulk-delete/', BulkDeleteAPIView.as_view(), name='bulk_delete'),

]
urlpatterns += router.urls
