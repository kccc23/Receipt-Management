from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.

def receipts_home(request):
    receipts = Receipt.objects.all()
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/receipts_list.html", context)