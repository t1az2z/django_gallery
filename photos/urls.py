# Набор URL для приложения Photos
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view, name="view"),
    url(r'^(?P<id>\d+)/$', views.detail, name="detail"),
    url(r'^upload/$', views.upload, name="upload"),
    url(r'^delete/$', views.delete, name="delete"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
