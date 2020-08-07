from datetime import timedelta, date
from django.conf import settings
from django.core.exceptions import ValidationError


def calcula_idade(nascimento, data_referencia=None):
    """
    Retorna a idade de uma pessoa na data_referencia (padrão: hoje).
    """

    if data_referencia is None:
        data_referencia = date.today()

    # Calcula a idade com base no ano de nascimento
    idade = data_referencia.year - nascimento.year

    # Subtrai 1 ano se a pessoa ainda não fez aniversário neste ano
    idade -= ((data_referencia.month, data_referencia.day) < (nascimento.month, nascimento.day))
    return idade


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
