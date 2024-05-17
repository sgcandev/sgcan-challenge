from dynamic_rest.routers import DynamicRouter
from transcripts.api.viewsets import TranscriptViewSet, SentenceViewSet

router = DynamicRouter()

router.register(r"transcripts", TranscriptViewSet)
router.register(r"sentences", SentenceViewSet)

urlpatterns = router.urls
