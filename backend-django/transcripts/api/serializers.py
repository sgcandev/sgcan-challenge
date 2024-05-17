from rest_framework import serializers

from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.fields import DynamicRelationField


from transcripts.models import Transcript, Sentence


class SentenceSerializer(DynamicModelSerializer):
    class Meta:
        model = Sentence
        name = "sentence"
        fields = "__all__"


class TranscriptSerializer(DynamicModelSerializer):
    sentences = DynamicRelationField(SentenceSerializer, many=True, deferred=True)

    class Meta:
        model = Transcript
        name = "transcript"
        fields = "__all__"
