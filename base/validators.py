import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class UppercaseValidator:
    def validate(self, password, user=None):
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                _("A senha deve conter pelo menos uma letra maiúscula."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Sua senha deve conter pelo menos uma letra maiúscula."
        )

class SpecialCharValidator:
    def validate(self, password, user=None):
        if not re.search(r'[\W_]', password): # \W é "não-letra/número", _ é underline
            raise ValidationError(
                _("A senha deve conter pelo menos um caractere especial."),
                code='password_no_special',
            )
            
    def get_help_text(self):
        return _(
            "Sua senha deve conter pelo menos um caractere especial."
        )