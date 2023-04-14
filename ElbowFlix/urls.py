from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import get_video, index, movies_json

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("movie/", movies_json, name="movies_json"),
    path("movie/<int:id>/", get_video, name="get_video"),
    path('user/',include('users.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
