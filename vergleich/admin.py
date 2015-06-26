from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Fahrzeug
from .models import Waffe
from .models import Art
from .models import Munition

admin.site.register(Fahrzeug)
admin.site.register(Waffe)
admin.site.register(Art)
admin.site.register(Munition)

