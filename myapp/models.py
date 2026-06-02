from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Registration(models.Model):

    First_name = models.CharField(max_length=200, null=True, blank=True)
    Last_name = models.CharField(max_length=200, null=True, blank=True)

    Email = models.EmailField(max_length=200, null=True, blank=True)
    Password = models.CharField(max_length=200, null=True, blank=True)

    Mobile_Number = models.CharField(max_length=200, null=True, blank=True)

    Registration_date = models.DateField(max_length=200, null=True, blank=True)

    Image = models.ImageField(upload_to='logo/', blank=True, null=True)

    gst_num = models.CharField(max_length=200, null=True, blank=True)

    address = models.TextField(max_length=1000, null=True, blank=True)

    User_Agreement = models.BooleanField(default=False)

    User_role = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    edit_allowed = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        default="False"
    )

    # SMTP Fields

    smtp_host = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        default='smtp.gmail.com'
    )

    smtp_port = models.IntegerField(
        null=True,
        blank=True,
        default=587
    )

    smtp_email = models.EmailField(
        max_length=200,
        null=True,
        blank=True
    )

    smtp_password = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    smtp_use_tls = models.BooleanField(default=True)
    payment_status=models.CharField(max_length=200, null=True, blank=True)
    payment_expiry= models.CharField(max_length=200, null=True, blank=True)



    def __str__(self):
        return self.First_name


class Branch(models.Model):
    location = models.CharField(max_length=255,null=True)
    created_at = models.DateField(auto_now_add=True,null=True, blank=True)
from django.contrib.auth.models import User  # or use get_user_model()

class Vendor(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    mobile_number = models.CharField(max_length=15,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Add this

    def __str__(self):
        return self.name



from django.contrib.auth.models import User  # or your custom user model
from decimal import Decimal

class Item(models.Model):
    name = models.CharField(max_length=255, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='items', null=True)
    company_name = models.CharField(max_length=100, null=True)
    gst = models.CharField(max_length=100, null=True)
    hsn = models.CharField(max_length=100, null=True)
    item_price = models.DecimalField(max_digits=100, decimal_places=2, default=Decimal('340.34'), null=True)
    pack_size = models.CharField(max_length=100, null=True)
    
    stock_balance = models.DecimalField(max_digits=100, decimal_places=2, default=Decimal('0.00'), null=True)  # Changed
    created_at = models.DateField(auto_now_add=True,null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name




class Company(models.Model):
    name = models.CharField(max_length=255,null=True)
    item = models.ForeignKey('Item', on_delete=models.CASCADE,null=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE,null=True)

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Company_line(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='line_ids',null=True)
    item_price = models.DecimalField(max_digits=100, decimal_places=2,default=340.34,null=True)
    pack_size = models.CharField(max_length=255,null=True)
    stock_balance = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    gst = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    hsn = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)


class ConsumedPurchaseOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='consumed_purchase_orders', null=True)
    invoice_number = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=255, null=True)
    dateField = models.DateField(null=True, blank=True) 
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Consumed-PO-{self.id} | {self.vendor.name if self.vendor else 'No Vendor'}"


class ConsumedPurchaseOrderLine(models.Model):
    consumed_order = models.ForeignKey(ConsumedPurchaseOrder, on_delete=models.CASCADE, related_name='consumed_lines')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    pack = models.CharField(max_length=100, null=True)
    stock = models.IntegerField(null=True)
    qty = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    gst = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    hsn = models.CharField(max_length=200, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.item.name if self.item else 'No Item'} - {self.qty} pcs (Consumed)"

class InvoiceCounter(models.Model):
    invoice_number = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


from django.utils.timezone import now
class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders', null=True)
    invoice_number = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=255, null=True)
    dateField = models.DateField(null=True, blank=True) 
    created_at = models.DateField(null=True, blank=True,default=now)  # 👈 Manual date entry allowed
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_confirmed = models.BooleanField(default=False,null=True, blank=True)  
    def __str__(self):
        return f"PO-{self.id} | {self.vendor.name if self.vendor else 'No Vendor'}"


class PurchaseOrderLine(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='order_lines')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    pack = models.CharField(max_length=100, null=True)
    stock = models.IntegerField(null=True)
    qty = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    gst = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    hsn = models.CharField(max_length=200, null=True, blank=True)
    cgst = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    sgst = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)  # 👈 Manual date entry instead of auto_now_add

    def __str__(self):
        return f"{self.item.name if self.item else 'No Item'} - {self.qty} pcs"
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
class Invoice(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True, blank=True)
    invoice_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)

    sub_total = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    total_cgst = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    total_sgst = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)

    amount_in_words = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=50, default="Draft", null=True, blank=True)
    method = models.CharField(max_length=50, default="Manual", null=True, blank=True)
    invoice_date= models.DateField( null=True, blank=True)
    dateField = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.invoice_number
class InvoiceLineItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='line_items', on_delete=models.CASCADE, null=True, blank=True)
    purchase_order_line = models.ForeignKey(PurchaseOrderLine, on_delete=models.CASCADE, null=True, blank=True)

    qty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rate = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    line_total = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    cgst_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    sgst_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    expiry_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)




class PurchaseOrderApproval(models.Model):
    purchase_order_line = models.OneToOneField('PurchaseOrderLine', on_delete=models.CASCADE, null=True)
    approval_status = models.BooleanField(default=False)  # New boolean field
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        item_name = self.purchase_order_line.item.name if self.purchase_order_line and self.purchase_order_line.item else "No Item"
        return f"Approval - {item_name} ({self.approval_status})"


class BillingActivity(models.Model):

    name = models.CharField(max_length=200)

    code = models.CharField(
        max_length=100,
        unique=True
    )

    charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name



class UsageLog(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    activity = models.ForeignKey(
        BillingActivity,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    charge_per_unit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total_charge = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    remarks = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.activity.name}"



class MonthlyInvoice(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    month = models.IntegerField()

    year = models.IntegerField()

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    transaction_id = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    payment_date = models.DateField(
        blank=True,
        null=True
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    generated_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            'user',
            'month',
            'year'
        )


class PaymentCollection(models.Model):

    invoice = models.OneToOneField(
        MonthlyInvoice,
        on_delete=models.CASCADE
    )

    transaction_id = models.CharField(
        max_length=200
    )

    amount_paid = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_date = models.DateField()

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.transaction_id