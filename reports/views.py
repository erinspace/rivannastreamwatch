# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from reports.serializers import ReportSerializer
from reports.models import Report

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


class ReportList(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

