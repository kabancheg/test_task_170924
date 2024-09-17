from django.urls import include, re_path

from .views import LogItemListView


app_name = "test"

urlpatterns = [
    re_path(r"^logitems/?$", LogItemListView.as_view(), name="logitem-list"),
]
