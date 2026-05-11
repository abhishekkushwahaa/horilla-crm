"""
Admin configuration for Activity models in Horilla.
"""

# Third-party imports (Django)
from django.contrib import admin

# Local imports
from .models import Activity

# Register your activity models here.

admin.site.register(Activity)
