from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # =============================================================================
    # Admin Panel Part
    # =============================================================================
    path("admin/", admin.site.urls),
    # =============================================================================
    # Applications and API Part
    # =============================================================================
    path("api/accounts/", include("accounts.urls", namespace="account")),
    path("api/products/", include("product.urls", namespace="product")),
    path("api/buckets/", include("file.urls", namespace="bucket")),
    # =============================================================================
    # Schema and Documentation Part
    # =============================================================================
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # =============================================================================
    #
    # =============================================================================
]
