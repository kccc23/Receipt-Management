from django.urls import path
from receipts.views import receipts_home, create_receipt

urlpatterns = [
    path("", receipts_home, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]