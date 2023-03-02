from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def receipts_home(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/receipts_list.html", context)

@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "form": form
    }
    return render(request, "receipts/create.html", context)

@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": categories,
    }
    return render(request, "receipts/categories_list.html", context)

@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts,
    }
    return render(request, "receipts/accounts_list.html", context)
