from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.

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
    



