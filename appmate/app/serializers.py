from rest_framework import serializers

from app.models import Sample, SAMPLE_FIELDS


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sample
        fields = SAMPLE_FIELDS
