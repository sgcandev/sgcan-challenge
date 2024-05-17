from transcripts.models import Sentence, Transcript
from transcripts.api.serializers import SentenceSerializer, TranscriptSerializer
from dynamic_rest.viewsets import DynamicModelViewSet


class SentenceViewSet(DynamicModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


class TranscriptViewSet(DynamicModelViewSet):
    queryset = Transcript.objects.all()
    serializer_class = TranscriptSerializer
