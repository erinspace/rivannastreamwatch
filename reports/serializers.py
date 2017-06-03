from django.contrib.auth.models import User, Group


from reports.models import Report
from rest_framework import serializers


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('user', 'lattitude', 'longitude', 'incident_type', 'details', 'picture', 'date')
