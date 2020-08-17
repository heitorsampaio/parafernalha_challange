from datetime import date


def calcula_idade(nascimento, data_referencia=None):
    """
    Retorna a idade de uma pessoa na data_referencia (padrão: hoje).
    """

    if data_referencia is None:
        data_referencia = date.today()

    # Calcula a idade com base no ano de nascimento
    idade = data_referencia.year - nascimento.year

    # Subtrai 1 ano se a pessoa ainda não fez aniversário neste ano
    idade -= ((data_referencia.month, data_referencia.day)
              < (nascimento.month, nascimento.day))
    return idade
