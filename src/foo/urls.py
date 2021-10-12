from django.contrib import admin
from django.urls import path
from django.urls import include
from foo.nasa import views as nasa_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foo.nasa.urls')),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
