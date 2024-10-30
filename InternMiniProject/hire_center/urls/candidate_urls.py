from rest_framework.routers import SimpleRouter

from hire_center.views.candidate import CandidateViewSet

router = SimpleRouter()
router.register(r"candidates", CandidateViewSet, basename="candidate")
urlpatterns = router.urls
