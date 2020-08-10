from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shop/',include('shop.urls')),
    url(r'^blog/',include('blog.urls')),
    url(r'^$/',views.index)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
