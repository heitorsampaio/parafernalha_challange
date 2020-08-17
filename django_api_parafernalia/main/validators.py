from datetime import timedelta, date
from django.conf import settings
from django.core.exceptions import ValidationError
from .funcs import calcula_idade


def validate_idade_minima(data_nascimento):
    """
    Valida se a data de nascimento tem a idade mínima configurada.
    """
    if data_nascimento is None:
        return data_nascimento

    validate_idade_minima.nascimento = data_nascimento
    idade = calcula_idade(data_nascimento)
    if idade < settings.IDADE_MINIMA:
        raise ValidationError(
            f'A idade mínima para cadastro no sistema é de {settings.IDADE_MINIMA} anos.')
    return data_nascimento
