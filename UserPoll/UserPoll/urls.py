from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from UserPoll.yasg import schema_view

from api_user_poll import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls), name='Api'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
