from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator


class LogItem(models.Model):
    UNKNOWN = 0
    GET = 1
    POST = 2
    PUT = 3
    PATCH = 4
    DELETE = 5
    HEAD = 6
    OPTION = 7
    METHOD_CHOICES = (
        (UNKNOWN, "unknown"),
        (GET, "get"),
        (POST, "post"),
        (PUT, "put"),
        (PATCH, "patch"),
        (DELETE, "delete"),
        (HEAD, "head"),
        (OPTION, "option"),
    )

    ip = models.CharField(max_length=64, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    method = models.PositiveSmallIntegerField(
        choices=METHOD_CHOICES,
        default=UNKNOWN,
        blank=True,
        null=True,
    )
    uri = models.TextField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    size = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(pow(2, 30))],
    )
