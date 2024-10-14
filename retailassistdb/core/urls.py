from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("add_sale/", views.add_sale, name="add_sale"),
    path("stock/", views.add_sale, name="stock"),
    path("sales/", views.add_sale, name="sales"),
    path("add_product/", views.add_sale, name="add_product"),
    path("add_customer/", views.add_sale, name="add_customer"),
    path("create_transaction/", views.create_transaction, name="create_transaction"),
    path("customers_list/", views.customer_list, name="customers_list"),
    path("product_list/", views.product_list, name="product_list"),
    path("transaction_list/", views.transaction_list, name="transaction_list"),
    path("update_stock/", views.update_stock, name="update_stock"),
    path("revenue_report/", views.revenue_report, name="revenue_report"),
    path("expense_report/", views.expense_report, name="expense_report"),
    path("data_analytics/", views.data_analytics, name="data_analytics"),
    path("add_supplier/", views.add_supplier, name="add_supplier"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("add_employee/", views.add_employee, name="add_employee"),
    path("employees_list/", views.employees_list, name="employees_list"),
    path("add_expense/", views.add_expense, name="add_expense"),
    path("add_revenue/", views.add_revenue, name="add_revenue"),
    
]