import re
# exemplos: datas, CPF, CEP e placas de carro.

def validar(cpf):
    if (cpf == None) or (len(cpf) < 11):
        return "Quantidade de caracteres do CPF invalido."
    
    pattern1 = r'[0-9][0-9][0-9]\.[0-9][0-9][0-9]\.[0-9][0-9][0-9]\-[0-9][0-9]'

    resultado1 = re.fullmatch(pattern1, cpf)
    if resultado1 == None:
        return "CPF invalido."
    return f"CPF valido -> {cpf}"