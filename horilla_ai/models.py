from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class AIChatHistory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ai_chat_history",
        verbose_name=_("User")
    )
    message = models.TextField(verbose_name=_("User Message"))
    response = models.TextField(verbose_name=_("AI Response"))
    model_id = models.CharField(max_length=100, verbose_name=_("Model ID"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("AI Chat History")
        verbose_name_plural = _("AI Chat Histories")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
