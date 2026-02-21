from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from horilla.menu import main_section_menu, sub_section_menu

@main_section_menu.register
class AskAISection:
    section = "ai"
    name = _("Ask AI")
    icon = "/assets/icons/chat.svg"
    position = -1

@sub_section_menu.register
class AskAISubSection:
    section = "ai"
    verbose_name = _("Ask AI")
    icon = "assets/icons/chat.svg"
    url = reverse_lazy("horilla_ai:ask_ai")
    app_label = "ai"
    position = 1
