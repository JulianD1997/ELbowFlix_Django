from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index,get_video,movies_json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='name'),
    path("movie/", movies_json, name="movies_json"),
    path('movie/<int:id>/',get_video,name='get_video')
    
    
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
