from django.contrib import admin
from django.urls import path, include
from core.views import LoginView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='url-login'),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



