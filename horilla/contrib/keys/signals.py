"""
Signals for the keys app
"""

# Third-party imports (Django)
from django.db.models.signals import post_save
from django.dispatch import receiver

# First party imports (Horilla)
from horilla.apps import apps
from horilla.auth.models import User
from horilla.urls import NoReverseMatch, reverse_lazy

# Local imports
from .models import ShortcutKey

DEFAULT_SHORTCUTS = [
    {"page": "/", "key": "H", "command": "alt"},
    {"page": "/my-profile-view/", "key": "P", "command": "alt"},
    {"page": "/regional-formating-view/", "key": "G", "command": "alt"},
    {"page": "/user-login-history-view/", "key": "L", "command": "alt"},
    {"page": "/user-holiday-view/", "key": "V", "command": "alt"},
    {"page": "/shortkeys/short-key-view/", "key": "K", "command": "alt"},
    {"page": "/user-view/", "key": "U", "command": "alt"},
    {"page": "/branches-view/", "key": "B", "command": "alt"},
]


OPTIONAL_APP_SHORTCUTS = [
    {
        "app": "horilla.contrib.dashboard",
        "url_name": "dashboard:dashboard_list_view",
        "key": "D",
        "command": "alt",
    },
    {
        "app": "horilla.contrib.reports",
        "url_name": "reports:reports_list_view",
        "key": "R",
        "command": "alt",
    },
    {
        "app": "horilla.contrib.calendar",
        "url_name": "calendar:calendar_view",
        "key": "I",
        "command": "alt",
    },
    {
        "app": "horilla.contrib.activity",
        "page": "/activity/activity-view/",
        "key": "Y",
        "command": "alt",
    },
]


def _resolve_shortcut_page(shortcut):
    if "page" in shortcut:
        return shortcut["page"]

    try:
        return str(reverse_lazy(shortcut["url_name"]))
    except (KeyError, NoReverseMatch):
        return None


@receiver(post_save, sender=User)
def create_all_default_shortcuts(sender, instance, created, **kwargs):
    """
    Create all default shortcut keys for a newly created user
    using a single bulk insert.
    """

    if not created:
        return

    predefined = list(DEFAULT_SHORTCUTS)
    for shortcut in OPTIONAL_APP_SHORTCUTS:
        app_name = shortcut.get("app")
        if app_name and not apps.is_installed(app_name):
            continue
        page = _resolve_shortcut_page(shortcut)
        if not page:
            continue
        predefined.append(
            {
                "page": page,
                "key": shortcut["key"],
                "command": shortcut["command"],
            }
        )

    shortcuts = [
        ShortcutKey(
            user=instance,
            page=item["page"],
            key=item["key"],
            command=item["command"],
            company=instance.company,
        )
        for item in predefined
    ]

    ShortcutKey.objects.bulk_create(shortcuts, ignore_conflicts=True)
