"""
This module registers Floating, Settings, My Settings, and Main Section menus
for the Horilla Dashboard app
"""

from horilla.menu import main_section_menu, sub_section_menu

# First party imports (Horilla)
from horilla.urls import reverse_lazy
from horilla.utils.translation import gettext_lazy as _


@main_section_menu.register
class HomeSection:
    """
    Registers the Home section in the main sidebar.
    """

    section = "home"
    name = _("Home")
    icon = "/assets/icons/home.svg"
    position = 0


@sub_section_menu.register
class DashboardSubSection:
    """
    Registers the dashboard to sub section in the main sidebar.
    """

    section = "analytics"
    verbose_name = _("Dashboards")
    icon = "assets/icons/dashboards.svg"
    url = reverse_lazy("dashboard:dashboard_list_view")
    app_label = "dashboard"
    perm = ["dashboard.view_dashboard", "dashboard.view_own_dashboard"]
    position = 2
    attrs = {
        "hx-boost": "true",
        "hx-target": "#mainContent",
        "hx-select": "#mainContent",
        "hx-swap": "outerHTML",
    }
