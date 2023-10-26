from hms.admin import admin_site
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin_site.urls),
    path('billing/', include('billing.urls')),
    path('authentication/', include('authentication.urls')),
    path('core/', include('core.urls')),
    path('patient/', include('patient.urls')),
    path('healthcare/', include('healthcare.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
