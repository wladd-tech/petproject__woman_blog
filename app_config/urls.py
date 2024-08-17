from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from app_config import settings
from women.views import page_not_found
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace='users')),
    path("", include("women.urls")),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()


handler404 = page_not_found


admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Известные женщины мира'