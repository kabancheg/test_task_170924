import json
from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils import timezone

import django_filters
from django_filters import rest_framework as filters

from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import OrderingFilter, IsoDateTimeFilter

from .models import LogItem
from .serializers import LogItemSerializer


class LogItemFilter(filters.FilterSet):
    timestamp_lte = IsoDateTimeFilter(
        field_name="timestamp", lookup_expr="lte", input_formats=["%d-%m-%Y"]
    )
    timestamp_gte = IsoDateTimeFilter(
        field_name="timestamp", lookup_expr="gte", input_formats=["%d-%m-%Y"]
    )

    class Meta:
        model = LogItem
        fields = ["size", "ip", "method", "timestamp", "status", "uri"]


class LogItemListView(generics.ListAPIView):
    serializer_class = LogItemSerializer
    http_method_names = (
        "get",
        "head",
    )
    permission_classes = (AllowAny,)
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = LogItemFilter

    def get_queryset(self):
        return LogItem.objects.all().order_by("timestamp")
