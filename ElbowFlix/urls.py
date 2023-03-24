from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='name')
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
