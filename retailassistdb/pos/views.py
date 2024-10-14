from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django import forms
from django.utils import timezone
from .models import (
    Transaction, Discount, Sale, SpecialDiscount, StockAlert, SalesAnalytics, CustomerAnalytics, 
    Payment, Receipt, Return, Refund
)

# Define forms for the models
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['product', 'customer', 'payment_method', 'total_amount', 'points_earned']

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['name', 'valid_from', 'valid_until', 'amount', 'special_conditions']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'transaction', 'employee', 'date', 'quantity', 'discount', 'subtotal', 'final_price', 'payment_method']

class SpecialDiscountForm(forms.ModelForm):
    class Meta:
        model = SpecialDiscount
        fields = ['product', 'name', 'amount', 'discount_percent', 'valid_until', 'special_conditions']

class StockAlertForm(forms.ModelForm):
    class Meta:
        model = StockAlert
        fields = ['product', 'threshold', 'date']

class SalesAnalyticsForm(forms.ModelForm):
    class Meta:
        model = SalesAnalytics
        fields = ['report_date', 'total_sales_value', 'top_selling_product', 'num_transactions']

class CustomerAnalyticsForm(forms.ModelForm):
    class Meta:
        model = CustomerAnalytics
        fields = ['customer', 'total_spent', 'total_loyalty_points_earned', 'total_loyalty_points_redeemed']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['transaction', 'method', 'amount']

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['transaction', 'receipt_number', 'sale', 'email']

class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ['sale', 'transaction', 'product', 'quantity', 'return_reason']

class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ['return_sale', 'transaction', 'amount']

def index(request):
    # Check if the session key 'visits' exists
    if 'visits' in request.session:
        # Increment the number of visits
        request.session['visits'] += 1
    else:
        # Initialize the number of visits
        request.session['visits'] = 1

    # Retrieve the number of visits from the session
    visits = request.session['visits']

    return render(request, "pos/dashboard.html", {'visits': visits})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, "pos/transaction_list.html", {"transactions": transactions})

def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:transaction_list')
    else:
        form = TransactionForm()
    return render(request, "pos/add_transaction.html", {"form": form})

def discount_list(request):
    discounts = Discount.objects.all()
    return render(request, "pos/discount_list.html", {"discounts": discounts})

def add_discount(request):
    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:discount_list')
    else:
        form = DiscountForm()
    return render(request, "pos/add_discount.html", {"form": form})

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, "pos/sale_list.html", {"sales": sales})

def add_sale(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:sale_list')
    else:
        form = SaleForm()
    return render(request, "pos/add_sale.html", {"form": form})

def special_discount_list(request):
    special_discounts = SpecialDiscount.objects.all()
    return render(request, "pos/special_discount_list.html", {"special_discounts": special_discounts})

def add_special_discount(request):
    if request.method == "POST":
        form = SpecialDiscountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:special_discount_list')
    else:
        form = SpecialDiscountForm()
    return render(request, "pos/add_special_discount.html", {"form": form})

def stock_alert_list(request):
    stock_alerts = StockAlert.objects.all()
    return render(request, "pos/stock_alert_list.html", {"stock_alerts": stock_alerts})

def add_stock_alert(request):
    if request.method == "POST":
        form = StockAlertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:stock_alert_list')
    else:
        form = StockAlertForm()
    return render(request, "pos/add_stock_alert.html", {"form": form})

def sales_analytics_list(request):
    sales_analytics = SalesAnalytics.objects.all()
    return render(request, "pos/sales_analytics_list.html", {"sales_analytics": sales_analytics})

def add_sales_analytics(request):
    if request.method == "POST":
        form = SalesAnalyticsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:sales_analytics_list')
    else:
        form = SalesAnalyticsForm()
    return render(request, "pos/add_sales_analytics.html", {"form": form})

def customer_analytics_list(request):
    customer_analytics = CustomerAnalytics.objects.all()
    return render(request, "pos/customer_analytics_list.html", {"customer_analytics": customer_analytics})

def add_customer_analytics(request):
    if request.method == "POST":
        form = CustomerAnalyticsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:customer_analytics_list')
    else:
        form = CustomerAnalyticsForm()
    return render(request, "pos/add_customer_analytics.html", {"form": form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, "pos/payment_list.html", {"payments": payments})

def add_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:payment_list')
    else:
        form = PaymentForm()
    return render(request, "pos/add_payment.html", {"form": form})

def receipt_list(request):
    receipts = Receipt.objects.all()
    return render(request, "pos/receipt_list.html", {"receipts": receipts})

def add_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:receipt_list')
    else:
        form = ReceiptForm()
    return render(request, "pos/add_receipt.html", {"form": form})

def return_list(request):
    returns = Return.objects.all()
    return render(request, "pos/return_list.html", {"returns": returns})

def add_return(request):
    if request.method == "POST":
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:return_list')
    else:
        form = ReturnForm()
    return render(request, "pos/add_return.html", {"form": form})

def refund_list(request):
    refunds = Refund.objects.all()
    return render(request, "pos/refund_list.html", {"refunds": refunds})

def add_refund(request):
    if request.method == "POST":
        form = RefundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos:refund_list')
    else:
        form = RefundForm()
    return render(request, "pos/add_refund.html", {"form": form})