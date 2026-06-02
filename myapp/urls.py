from django.urls import path
from . import views
from django.contrib import admin
from .views import  admin_home
from django.db import models
from django.contrib.auth.models import User


urlpatterns = [
    path('',views.home,name = 'home'),
    path('home',views.home,name = 'home'),
    path('adminn',views.admin_rg,name = 'adminn'),
    path('delete_admin', views.delete_admin, name='delete_admin'),
    path('edit_admin', views.edit_admin, name='edit_admin'),
    path('admin_rg',views.admin_rg, name='admin_rg'),
    path('bnb', views.bnb, name='bnb'),
    path('del_admin/<id>', views.del_admin, name='del_admin'),
      path('del_employee/<id>', views.del_employee, name='del_employee'),
    path('edit_admin',views.edit_admin, name='edit_admin'),
    path('logged_out', views.logged_out, name='logged_out'),
    path('login/',views.login,name = 'login'),
    path('logout', views.logout, name='logout'),
    path('admin_home',views.admin_home, name='admin_home'),
    path('adminn_details', views.adminn_details, name='adminn_details'),
    path('register_employee', views.register_employee, name='register_employee'),
        path('employeess', views.employeess, name='employeess'),
        path('dashboard', views.employee_home, name='employee_home'),
        path('update_employee', views.update_employee, name='update_employee'),
        path('update_employeee', views.update_employeee, name='update_employeee'),
path('view_branches', views.view_staffs, name='view_staffs'),
path('update_employeee/<int:employee_id>/', views.update_employeee, name='update_employeee'),

  path('branch_list', views.branch_list, name='branch_list'),
    path('branch_create', views.branch_create, name='branch_create'),
    path('branch_detail/<int:pk>/', views.branch_detail, name='branch_detail'),
    path('branch_update/<int:pk>/edit/', views.branch_update, name='branch_update'),
    path('branch_delete/<int:pk>/delete/', views.branch_delete, name='branch_delete'),

    path('company_list', views.company_list, name='company_list'),
    path('get_companies/', views.get_companies, name='get_companies'),

path('view_po/', views.view_po_items, name='view_po'),
path('view_purchase/', views.view_po_items_admin, name='view_po_admin'),
path('placed_orders/', views.placed_orders, name='placed_orders'),
path('orders/', views.placed_orders_all, name='placed_orders_all'),
path('generate_invoice/<int:item_id>/', views.generate_invoice, name='generate_invoice'),
    path('download_excel/', views.download_excel, name='download_excel'),
    path('company_create', views.company_create, name='company_create'),
    path('companies/update/<int:pk>/', views.company_update, name='company_update'),
path('companies/delete/<int:pk>/', views.company_delete, name='company_delete'),

path('get-items/<int:vendor_id>/', views.get_items_by_vendor, name='get_items_by_vendor'),

    path('vendor_list', views.vendor_list, name='vendor_list'),
        path('vendor_list_admin', views.vendor_list_admin, name='vendor_list_admin'),
    path('vendors/create/', views.vendor_create, name='vendor_create'),
    path('vendors/update/<int:pk>/', views.vendor_update, name='vendor_update'),
    path('vendors/delete/<int:pk>/', views.vendor_delete, name='vendor_delete'),
        path('vendors/delete/admin<int:pk>/', views.vendor_delete_admin, name='vendor_delete_admin'),

    path('item', views.item_list_admin, name='item_list_admin'),
   
    path('item_list', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/update/<int:pk>/', views.item_update, name='item_update'),
    path('items/delete/<int:pk>/', views.item_delete, name='item_delete'),
        path('items/delete/admin/<int:pk>/', views.item_delete_admin, name='item_delete_admin'),

  path('purchase_order_item/delete/<int:pk>/', views.purchase_order_item_delete, name='purchase_order_item_delete'),

  path('generate_invoice/', views.generate_invoice, name='generate_invoice'),


    path('download_pdf/<str:invoice_number>/', views.download_pdf, name='download_pdf'),
    path('generate_invoice/', views.generate_invoice, name='generate_invoice'),
    path('download_pdf/<str:invoice_number>/', views.download_pdf, name='download_pdf'),
 path('placed_orders/<int:vendor_id>/', views.placed_orders, name='placed_orders'),

 path('invoice/delete/<int:pk>/', views.invoice_delete_admin, name='invoice_delete_admin'),
 path('invoice/delete/<int:pk>/', views.invoice_delete, name='invoice_delete'),
 path('invoice/edit/<int:pk>/', views.invoice_edit, name='invoice_edit'),

 path('invoices/bulk-delete/', views.invoice_bulk_delete, name='invoice_bulk_delete'),
path('invoice/view/<str:invoice_number>/', views.view_invoice, name='view_invoice'),
path('view_purchase_order', views.view_purchase_order, name='view_purchase_order'),

  path("download_database/",views.download_database,name="download_database"),



      path('invoice_admin/view/<str:invoice_number>/', views.view_invoice_admin, name='view_invoice_admin'),


    path('purchase/create/', views.create_purchase_order, name='create_purchase_order'),

    path('view_purchase_orders/', views.view_purchase_orders, name='view_purchase_orders'),
 path('purchase-orders/<int:po_id>/edit/', views.edit_purchase_order, name='edit_purchase_order'),
    path('purchase-orders/<int:po_id>/delete/', views.delete_purchase_order, name='delete_purchase_order'),



    path('send-invoice-email/<int:invoice_id>/', views.send_invoice_email, name='send_invoice_email'),
    path('upload-invoice-for-whatsapp/<int:invoice_id>/', views.upload_invoice_for_whatsapp, name='upload_invoice_for_whatsapp'),





 path('get-item-details/', views.get_item_details, name='get_item_details'),
 

 path('get-vendor-details/', views.get_vendor_details, name='get_vendor_details'),

  path('consumed/create/', views.create_consumed_order, name='create_consumed_order'),
    path('consumed/edit/<int:consumed_po_id>/', views.edit_consumed_order, name='edit_consumed_order'),
    path('consumed/delete/<int:consumed_po_id>/', views.delete_consumed_order, name='delete_consumed_order'),

    # Optional: List or view all consumed purchase orders
    path('view_consumed_orders', views.view_consumed_orders, name='view_consumed_orders'), 
    
     # Define this view if needed
    path('custom_consumed', views.custom_consumed, name='custom_consumed'), 
path('invoice/preview/<int:pk>/', views.preview_invoice, name='preview_invoice'),

path('invoices/preview/<int:pk>/', views.preview_invoices, name='preview_invoices'),

        path('view_consumption', views.view_consumption, name='view_consumption'),  # Define this view if needed








    path('invoices/', views.view_invoices, name='view_invoices'),
    path('invoice/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('create-invoice/<int:pk>/', views.create_invoice_from_po, name='create_invoice_from_po'),










        #---------------------------------place  purchase order--------------
        path('purchase-order/place/<int:pk>/', views.place_purchase_order, name='place_purchase_order'),


    path('purchase-order/<int:pk>/invoice/', views.purchase_order_invoice, name='purchase_order_invoice'),

    path('get-item-details/', views.get_item_details, name='get_item_details'),



#-----------send email------------------


# app/urls.py

    path('send-purchase-order-email/', views.send_purchase_order_email, name='send_purchase_order_email'),
    path('upload-invoice-for-whatsapp/', views.upload_invoice_for_whatsapp, name='upload_invoice_for_whatsapp'),

    path('purchase-order/<int:pk>/approve/', views.approve_po_items, name='approve_po_items'),
path('invoice/<int:pk>/', views.invoice_view, name='purchase_order_invoice'),


    path('invoice/<int:pk>/', views.invoice_view, name='purchase_order_invoice'),  # This is critical

    path('purchase-order/<int:pk>/', views.purchase_order_detail, name='purchase_order_detail'),
    # other paths...
 path('invoice/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),
# In your app's urls.py

    path('purchase-order/<int:pk>/create-invoice/', views.create_invoice_from_po, name='create_invoice_from_po'),
path('invoices/<int:pk>/', views.invoice_detail, name='invoice_detail'),
path('purchase-order/<int:pk>/', views.purchase_order_detail, name='purchase_order_detail'),
path('view_purchase_orders/', views.view_purchase_orders, name='view_purchase_orders'),
path('consumed-order/update/<int:order_id>/', views.update_consumed_order, name='update_consumed_order'),
    path('api/vendor/<int:vendor_id>/', views.get_vendor_data, name='get_vendor_data'),
    path('api/item/<int:item_id>/', views.get_item_data, name='get_item_data'),
path('purchase-order/update/<int:po_id>/', views.update_purchase_order, name='update_purchase_order'),


path('bulk-delete/', views.vendor_bulk_delete, name='vendor_bulk_delete'),  # Bulk delete

        path('bulk-delete/', views.item_bulk_delete, name='item_bulk_delete'), # Bulk delete
      path('items/import-excel/', views.item_import_excel, name='item_import_excel'),
path('import-excel/', views.vendor_import_excel, name='vendor_import_excel'),  # Optional: Excel import

    path('get-item-details/', views.get_item_details, name='get_item_details'),
    path('get-vendor-details/', views.get_vendor_details, name='get_vendor_details'),

path('purchase-order/<int:pk>/undo-invoice/', views.undo_invoice_from_po, name='undo_invoice_from_po'),





path("items/bulk-delete/", views.item_bulk_delete, name="item_bulk_delete"),

  path('bulk_delete_purchase_orders/', views.bulk_delete_purchase_orders, name='bulk_delete_purchase_orders'),

path(
    "bulk_delete_consumed_orders/",
    views.bulk_delete_consumed_orders,
    name="bulk_delete_consumed_orders"
),


path('toggle-edit/<int:id>/', views.toggle_edit, name='toggle_edit'),
    path("edit_employee/<int:id>",views.edit_employee,name="edit_employee"),
path('payment/', views.payment_page),
path('create-order/', views.create_order),
path('payment-success/', views.payment_success),
path(
    'billing-activities/',
    views.billing_activity_list,
    name='billing_activity_list'
),

path(
    'billing-activity-add/',
    views.billing_activity_add,
    name='billing_activity_add'
),

path(
    'billing-activity-edit/<int:id>/',
    views.billing_activity_edit,
    name='billing_activity_edit'
),

path(
    'billing-activity-delete/<int:id>/',
    views.billing_activity_delete,
    name='billing_activity_delete'
),
path(
    'usage-logs/',
    views.usage_logs,
    name='usage_logs'
),
path(
    'branch-billing-summary/',
    views.branch_billing_summary,
    name='branch_billing_summary'
),
path(
    'branch-billing-detail/<int:user_id>/',
    views.branch_billing_detail,
    name='branch_billing_detail'
),
path(
    'monthly-invoices/',
    views.monthly_invoice_list,
    name='monthly_invoice_list'
),

path(
    'generate-monthly-invoices/',
    views.generate_monthly_invoices,
    name='generate_monthly_invoices'
),

path(
    'invoice-payment/<int:id>/',
    views.invoice_payment,
    name='invoice_payment'
),

]
