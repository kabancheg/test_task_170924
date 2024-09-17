import json
from datetime import datetime

from django.core.management.base import BaseCommand

# from django.utils import timezone

from test.models import LogItem
from test.serializers import LogItemSerializer


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("path", type=str)

    def handle(self, *args, **kwargs):
        path = str(kwargs["path"])
        data = []
        method_mapping = dict([(i[1], i[0]) for i in LogItem.METHOD_CHOICES])
        with open(path, "r") as file:
            for r in file.readlines():
                d = json.loads(r)
                uri, method = "", LogItem.UNKNOWN
                try:
                    uri = str(d["request"]).split(" ")[1]
                    method = method_mapping[str(d["request"]).split(" ")[0].lower()]
                except (IndexError, KeyError):
                    pass

                timestamp = None
                try:
                    timestamp = datetime.strptime(d["time"], "%d/%b/%Y:%H:%M:%S +%f")
                except ValueError:
                    pass

                s = LogItemSerializer(
                    data={
                        "ip": d["remote_ip"],
                        "status": d["response"],
                        "size": int(d["bytes"]),
                        "timestamp": timestamp,
                        "method": method,
                        "uri": uri,
                    }
                )
                if s.is_valid(raise_exception=False):
                    data.append(LogItem(**s.validated_data))

        LogItem.objects.bulk_create(data)
