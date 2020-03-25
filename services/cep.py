
import re
# exemplos: datas, CPF, CEP e placas de carro.

def validar(cep):
    if cep == None or len(cep) <= 7:
        return "Quantidade de caracteres de CEP é menos do que esperado."
    
    pattern1 = r'[0-9][0-9][0-9][0-9][0-9]\-[0-9][0-9][0-9]'
    pattern2 = r'[0-9][0-9]\.[0-9][0-9][0-9]\-[0-9][0-9][0-9]'

    resultado1 = re.fullmatch(pattern1, cep)
    resultado2 = re.fullmatch(pattern2, cep)
    if resultado1 == None:
        if resultado2 == None:
            return "CEP invalida."
    return f"CEP valida -> {cep}"
