from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("codelists.urls")),
    path("admin/", admin.site.urls),
    path("ctv3/", include("coding_systems.ctv3.urls")),
    path("snomedct/", include("coding_systems.snomedct.urls")),
    path("api/v1/snomedct/", include("coding_systems.snomedct.api_urls")),
]
