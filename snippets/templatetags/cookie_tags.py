# snippets/templatetags/cookie_tags.py

from django import template
from snippets.models import CookieConsent

register = template.Library()

@register.inclusion_tag("snippets/cookie_banner.html", takes_context=True)
def cookie_banner(context):
    try:
        cookie_consent = CookieConsent.objects.first()
        expected_version = cookie_consent.version if cookie_consent else 1
    except CookieConsent.DoesNotExist:
        cookie_consent = None
        expected_version = 1

    return {"cookie_consent": cookie_consent, "expected_version": expected_version}



