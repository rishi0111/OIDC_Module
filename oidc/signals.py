from django.dispatch import receiver
from django.urls import reverse
from pretalx.orga.signals import nav_event_settings


@receiver(nav_event_settings)
def oidc_settings(sender, request, **kwargs):
    if not request.user.has_perm("orga.change_settings", request.event):
        return []
    return [
        {
            "label": "OIDC_AUTHENTICATION",
            "url": reverse(
                "plugins:oidc:settings",
                kwargs={"event": request.event.slug},
            ),
            "active": request.resolver_match.url_name == "plugins:oidc:settings",
        }
    ]
