from rest_framework import routers
from .views import DashboardAppointmentViewSet, DayViewSet, DepartmentViewSet,DoctorViewSet,ScheduleViewSet,AppointmentViewSet,BedViewSet, BedAssignViewSet,BirthReportViewSet,DeathReportViewSet,CountSummaryView
from django.urls import path



router = routers.DefaultRouter()
router.register('departments', DepartmentViewSet,basename='department')
router.register('doctors', DoctorViewSet,basename='doctor')
router.register('schedules', ScheduleViewSet,basename='schedule')
router.register('days', DayViewSet,basename='day')
router.register('appointments', AppointmentViewSet,basename='appointment')
router.register('dashboard/appointments', DashboardAppointmentViewSet,basename='dashboard-appointment')
router.register('beds', BedViewSet,basename='bed')
router.register('bed-assigns', BedAssignViewSet,basename='bed-assign')
router.register('birth-reports', BirthReportViewSet,basename='birth-report')
router.register('death-reports', DeathReportViewSet,basename='death-report')

urlpatterns = [
    path('count-members',CountSummaryView.as_view(),name='count-members'),
]

urlpatterns += router.urls