from rest_framework.routers import SimpleRouter

from hire_center.views.company import CompanyViewSet

router = SimpleRouter()
router.register(r"companies", CompanyViewSet, basename="company")
urlpatterns = router.urls
