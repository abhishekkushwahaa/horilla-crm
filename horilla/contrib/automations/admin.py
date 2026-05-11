"""
Admin registration for the automations app
"""

# Third-party imports (Django)
from django.contrib import admin

# Local imports
from .models import AutomationCondition, AutomationRunLog, HorillaAutomation

# Register your automations models here.

admin.site.register(HorillaAutomation)
admin.site.register(AutomationCondition)
admin.site.register(AutomationRunLog)
