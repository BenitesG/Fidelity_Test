# base/widgets.py
from django_recaptcha.widgets import ReCaptchaBase
from django.utils.safestring import mark_safe
from django.conf import settings

# Clean Captcha error message bug
class CleanReCaptchaV2Checkbox(ReCaptchaBase):
    template_name = None 

    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        extra = " ".join(f'{k}="{v}"' for k, v in attrs.items())
        html = f'<div class="g-recaptcha" data-sitekey="{settings.RECAPTCHA_PUBLIC_KEY}" {extra}></div>'
        return mark_safe(html)
