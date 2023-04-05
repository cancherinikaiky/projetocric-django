
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('cidades/', include('cities.urls')),
    path('sobre/', include('about.urls')),
    path('manual/', include('manual.urls')),
    path('contato/', include('contact.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
