from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt

# Register your models here.

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "id",
    )

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "owner",
        "id",
    )

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "total",
        "vendor",
        "id",
    )