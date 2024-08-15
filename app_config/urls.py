from django.contrib import admin
from django.urls import include, path
from women.views import page_not_found
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("women.urls")),
] + debug_toolbar_urls()


handler404 = page_not_found


admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Известные женщины мира'