from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import Employee, Supplier
# Create your views here.

class AddEmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)
    email = forms.EmailField()

class AddSupplierForm(forms.Form):
    name = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=100)
    email = forms.EmailField()

class AddSaleForm(forms.Form):
    product_id = forms.ChoiceField(choices=[])  # Populate choices dynamically in the view
    quantity = forms.IntegerField(min_value=1)

class CreateTransactionForm(forms.Form):
    # Define your form fields here
    pass

class AddCustomerForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

class AddProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = forms.IntegerField(min_value=0)

class UpdateStockForm(forms.Form):
    product_id = forms.ChoiceField(choices=[])  # Populate choices dynamically in the view
    quantity = forms.IntegerField(min_value=1)
class AddExpenseForm(forms.Form):
    description = forms.CharField(max_length=255)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    date = forms.DateField(widget=forms.SelectDateWidget)

class AddRevenueForm(forms.Form):
    description = forms.CharField(max_length=255)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    date = forms.DateField(widget=forms.SelectDateWidget)

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

    return render(request, "core/dashboard.html", {'visits': visits})

def add_sale(request):
    if request.method == "POST":
        form = AddSaleForm(request.POST)
        if form.is_valid():
            # Handle form submission logic here
            sale = form.cleaned_data
            # Add the new sale to the session
            request.session['sales_list'] = request.session.get('sales_list', []) + [sale]
            return HttpResponseRedirect(reverse("core:transaction_list"))
    else:
        form = AddSaleForm()
        # Populate product choices dynamically
        form.fields['product_id'].choices = [(product.id, product.name) for product in []]  # Replace with actual product fetching logic
    return render(request, "core/add_sale.html", {'form': form})

def create_transaction(request):
    if request.method == "POST":
        form = CreateTransactionForm(request.POST)
        if form.is_valid():
            # Handle form submission logic here
            transaction = form.cleaned_data
            # Add the new transaction to the session
            request.session['transactions_list'] = request.session.get('transactions_list', []) + [transaction]
            return HttpResponseRedirect(reverse("core:transaction_list"))
    else:
        form = CreateTransactionForm()
    return render(request, "core/create_transaction.html", {'form': form})

def customer_list(request):
    # Fetch customer data from the database
    customers = request.session.get('customers_list', [])  # Replace with actual data fetching logic
    return render(request, "core/customers_list.html", {"customers": customers})

def product_list(request):
    # Fetch product data from the database
    products = request.session.get('products_list', [])  # Replace with actual data fetching logic
    return render(request, "core/product_list.html", {"products": products})

def transaction_list(request):
    # Fetch transaction data from the database
    transactions = request.session.get('transactions_list', [])  # Replace with actual data fetching logic
    return render(request, "core/transaction_list.html", {"transactions": transactions})

def update_stock(request):
    if request.method == "POST":
        form = UpdateStockForm(request.POST)
        if form.is_valid():
            # Handle form submission logic here
            stock_update = form.cleaned_data
            # Add the stock update to the session
            request.session['stock_updates'] = request.session.get('stock_updates', []) + [stock_update]
            return HttpResponseRedirect(reverse("core:product_list"))
    else:
        form = UpdateStockForm()
        # Populate product choices dynamically
        form.fields['product_id'].choices = [(product.id, product.name) for product in []]  # Replace with actual product fetching logic
    return render(request, "core/update_stock.html", {'form': form})

def stock(request):
    if "stock" not in request.session:
        # If not, create a new list
        request.session["stock"] = []
    return render(request, "core/stock.html", {"stock": request.session["stock"]})

def add_customer(request):
    if request.method == "POST":
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            # Isolate the new customer from the 'cleaned' version of form data
            customer = form.cleaned_data["name"]
            # Add the new customer to our list of customers
            request.session["customers_list"] = request.session.get("customers_list", []) + [customer]
            # Redirect user to list of customers
            return HttpResponseRedirect(reverse("customer_list"))
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "core/add_customer.html", {"form": form})
    return render(request, "core/add_customer.html", {"form": AddCustomerForm()})

def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            # Isolate the new product from the 'cleaned' version of form data
            product = form.cleaned_data["name"]
            # Add the new product to our list of products
            request.session["products_list"] = request.session.get("products_list", []) + [product]
            # Redirect user to list of products
            return HttpResponseRedirect(reverse("product_list"))
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "core/add_product.html", {"form": form})
    return render(request, "core/add_product.html", {"form": AddProductForm()})

def sales(request):
    if "sales" not in request.session:
        # If not, create a new list
        request.session["sales"] = []
    return render(request, "core/sales.html", {"sales": request.session["sales"]})

def add_employee(request):
    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            # Handle form submission logic here
            employee = form.cleaned_data
            # Add the new employee to the session
            request.session['employees_list'] = request.session.get('employees_list', []) + [employee]
            return HttpResponseRedirect(reverse("core:employees_list"))
        else:
            return render(request, "core/add_employee.html", {"form": form})
    return render(request, "core/add_employee.html", {"form": AddEmployeeForm()})

def employees_list(request):
    employees = request.session.get('employees_list', [])
    return render(request, "core/employees_list.html", {"employees": employees})

def add_supplier(request):
    if request.method == "POST":
        form = AddSupplierForm(request.POST)
        if form.is_valid():
            # Handle form submission logic here
            supplier = form.cleaned_data
            # Add the new supplier to the session
            request.session['suppliers_list'] = request.session.get('suppliers_list', []) + [supplier]
            return HttpResponseRedirect(reverse("core:suppliers"))
        else:
            return render(request, "core/add_supplier.html", {"form": form})
    return render(request, "core/add_supplier.html", {"form": AddSupplierForm()})

def suppliers(request):
    suppliers = request.session.get('suppliers_list', [])
    return render(request, "core/suppliers.html", {"suppliers": suppliers})

def revenue_report(request):
    # Fetch revenue data from the database or session
    revenue_data = request.session.get('revenue_data', [])
    return render(request, "core/revenue_report.html", {"revenue_data": revenue_data})

def expense_report(request):
    # Fetch expense data from the database or session
    expense_data = request.session.get('expense_data', [])
    return render(request, "core/expense_report.html", {"expense_data": expense_data})

def data_analytics(request):
    # Fetch analytics data from the database or session
    analytics_data = request.session.get('analytics_data', [])
    return render(request, "core/data_analytics.html", {"analytics_data": analytics_data})

def add_expense(request):
    if request.method == "POST":
        form = AddExpenseForm(request.POST)
        if form.is_valid():
            # Handle form submission logic here
            expense = form.cleaned_data
            # Add the new expense to the session
            request.session['expense_data'] = request.session.get('expense_data', []) + [expense]
            return HttpResponseRedirect(reverse("core:expense_report"))
        else:
            return render(request, "core/add_expense.html", {"form": form})
    return render(request, "core/add_expense.html", {"form": AddExpenseForm()})

def add_revenue(request):
    if request.method == "POST":
        form = AddRevenueForm(request.POST)
        if form.is_valid():
            # Handle form submission logic here
            revenue = form.cleaned_data
            # Add the new revenue to the session
            request.session['revenue_data'] = request.session.get('revenue_data', []) + [revenue]
            return HttpResponseRedirect(reverse("core:revenue_report"))
        else:
            return render(request, "core/add_revenue.html", {"form": form})
    return render(request, "core/add_revenue.html", {"form": AddRevenueForm()})