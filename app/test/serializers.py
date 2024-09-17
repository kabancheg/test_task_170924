from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings

from rest_framework import serializers

from .models import LogItem


class LogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogItem
        fields = "__all__"
