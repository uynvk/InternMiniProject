from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from icenter.views.api import ApiViewSet
from icenter.views.api_version import ApiVersionViewSet

router = SimpleRouter()
router.register(r"apis", ApiViewSet, basename="api")

version_router = NestedSimpleRouter(router, r"apis", lookup="api")
version_router.register(r"versions", ApiVersionViewSet, basename="api-version")
urlpatterns = router.urls
urlpatterns += version_router.urls
