from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from core.views import custom_404

urlpatterns = [
    path('', include('core.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'core.views.custom_404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)