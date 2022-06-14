from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import apiv1_urls


urlpatterns = [
    path(
        route='api/v1/',
        view=include(apiv1_urls),
        name='apiv1_urls'
    ),
    path(
        route='test_app/',
        view=include('test_app.urls')
    ),
    path(
        route='__debug__/',
        view=include('debug_toolbar.urls')
    ),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
