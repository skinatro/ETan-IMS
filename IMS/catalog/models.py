from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", _("Admin")
        CUSTOMER = "customer", _("Customer")

    pid = models.IntegerField(unique=True, null=True, blank=True)
    role = models.CharField(
        max_length=10, choices=Role, default=Role.CUSTOMER
    )
    phone_number = models.CharField(
        max_length=10, unique=True, null=True, blank=True
    )
    is_member = models.BooleanField(default=False)

    def __str__(self):
        return self.email or self.username


class Component(models.Model):
    class Category(models.TextChoices):
        AC = "AC", _("Active Components")
        PAS = "PAS", _("Passive Components")
        SEMIC = "SEMIC" , _("Semiconductor Devices")
        PS = "PS" , _("Power Supplies")
        EMECH = "EMECH" , _("Electromechanical Components")
        SENS = "SENS" , _("Sensors")
        MC = "MC" , _("Microcontrollers")
        DLC = "DLC",_("Digital Logic Components")
        COMM = "COMM", _("Communicaton Modules")
        DISP = "DISP", _("Display Devices")
        SWITCH = "SWITCH", _("Switches and Protective Devices")
        CONN = "CONN", _("Connectors and Interfacing")
        WIRE = "WIRE", _("Wiring and Cables")
        PCB = "PCB", _("PCB and Prototypes")
        MECH = "MECH", _("Mechanical Componenets")
        TOOL = "TOOL", _("Tools and Test Equipment")
        MISC = "MISC", _("Miscellaneous")

    name = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=10, choices=Category,default=Category.MISC, null=False)

    quantity = models.IntegerField(default=0,null=False)
    is_rentable = models.BooleanField(default=True, null=False)
    rental_rate = models.IntegerField(default=0, null=False)
    product_image = models.ImageField(upload_to="product_images/",blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now,editable=False)
    datasheet_url = models.URLField(null=True)
    description = models.TextField(default="Component Specifications here")
    location = models.CharField(max_length=255, null=False, default="Cupboard")    

    def __str__(self):
        return self.name


class Order(models.Model):
    class Status(models.TextChoices):
        BOOKED = "booked", _("Booked")
        ACCEPTED = "accepted", _("Accepted")
        REJECTED = "rejected", _("Rejected")
        CANCELLED = "cancelled", _("Cancelled")
        RETURNED = "returned", _("Returned")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    status = models.CharField(
        max_length=10, choices=Status, default=Status.BOOKED
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    decided_at = models.DateTimeField(null=True, blank=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items"
    )
    component = models.ForeignKey(
        Component, on_delete=models.CASCADE, related_name="order_items"
    )
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ("order", "component")

    def __str__(self):
        return f"{self.component.name} x{self.quantity}"
