from django.urls import path
from receipts.views import receipts_home

urlpatterns = [
    path("", receipts_home, name="home"),
]