from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "oidc"
    verbose_name = "OIDC_AUTHENTICATION"

    class PretalxPluginMeta:
        name = gettext_lazy("OIDC_AUTHENTICATION")
        author = "Rishi"
        description = gettext_lazy("SSO")
        visible = True
        version = "1.0.0"
        category = "FEATURE"

    def ready(self):
        from . import signals  # NOQA
