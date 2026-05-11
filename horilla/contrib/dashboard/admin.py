"""Admin configuration for dashboard app."""

# Third-party imports (Django)
from django.contrib import admin

# Local imports
from .models import (
    ComponentCriteria,
    Dashboard,
    DashboardComponent,
    DashboardFolder,
    DefaultHomeLayoutOrder,
)

# Register your dashboard models here.
admin.site.register(Dashboard)
admin.site.register(DashboardComponent)
admin.site.register(ComponentCriteria)
admin.site.register(DashboardFolder)
admin.site.register(DefaultHomeLayoutOrder)
