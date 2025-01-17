from django.contrib import admin
from .models import Scenario

# Registering the Scenario model so it can be managed via the admin interface
admin.site.register(Scenario)
