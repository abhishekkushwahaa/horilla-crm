"""
Version and metadata information for the keys module.
"""

# First party imports (Horilla)
from horilla.utils.translation import gettext_lazy as _

__version__ = "1.10.0"
__module_name__ = "Short Keys"
__release_date__ = ""
__description__ = _("Module providing customizable keyboard shortcuts.")
__icon__ = "keys/assets/icons/icon3.svg"

__1_10_0__ = _(
    "Release 1.10: keyboard shortcuts ship under contrib with app label keys. "
    "URLs, registrations, shortcuts metadata, templates, and static paths "
    "updated from the legacy keys package layout."
)

__1_1_0__ = _(
    "Migrated from Django AppConfig to Horilla AppLauncher and replaced Django"
    "utilities with horilla.utils.decorators, horilla.utils.translation, and horilla.shortcuts where applicable."
)
