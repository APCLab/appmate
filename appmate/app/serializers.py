from rest_framework import serializers

from app.models import Sample


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sample
        fields = (
            'id', 'name', 'msg', 'date', 'timestamp', 'img', 'checked', 'email',
            'index')
