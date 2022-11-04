from django.contrib import admin
from .models import *

admin.site.register(Food_category)
admin.site.register(Menu)
admin.site.register(Dispatcher)
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Order)
admin.site.register(Order_details)
admin.site.register(Distribution)

# Register your models here.
