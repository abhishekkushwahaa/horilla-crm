"""Admin registrations for the `horilla.contrib.reports.urls` app."""

# Third-party imports (Django)
from django.contrib import admin

# Local imports
from . import models

# Register your reports models here.

admin.site.register(models.ReportFolder)
admin.site.register(models.Report)
