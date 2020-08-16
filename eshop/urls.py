from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from eshop.settings import MEDIA_URL,MEDIA_PATH

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
]+static(MEDIA_URL,document_root=MEDIA_PATH)
