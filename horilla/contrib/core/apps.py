"""
Horilla Core App configuration.
Handles app setup, demo data, and scheduler,signals and menu initialization.
"""

# First party imports (Horilla)
from horilla.apps import AppLauncher
from horilla.utils.translation import gettext_lazy as _


class CoreConfig(AppLauncher):
    """
    Configuration for the Horilla Core application.
    Includes URL registration and optional scheduler,signals and menu startup.
    """

    default = True

    default_auto_field = "django.db.models.BigAutoField"
    name = "horilla.contrib.core"
    label = "core"
    verbose_name = _("Core System")

    url_prefix = ""
    url_module = "horilla.contrib.core.urls"
    url_namespace = "core"

    auto_import_modules = [
        "registration",
        "signals",
        "scheduler",
        "login_history",
        "menu",
    ]

    celery_schedule_module = "celery_schedules"

    demo_data = {
        "files": [
            (1, "load_data/company.json"),
            (2, "load_data/role.json"),
            (3, "load_data/users.json"),
        ],
        # Optional fields (key & display_name will be auto-generated if not provided)
        "key": "users_count",
        "display_name": _("Users"),
        "order": 1,
    }

    def get_api_paths(self):
        """
        Return API path configurations for this app.

        Returns:
            list: List of dictionaries containing path configuration
        """
        return [
            {
                "pattern": "core/",
                "view_or_include": "horilla.contrib.core.api.urls",
                "name": "core_api",
                "namespace": "core",
            }
        ]
