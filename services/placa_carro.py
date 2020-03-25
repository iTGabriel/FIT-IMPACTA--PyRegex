
import re
# exemplos: datas, CPF, CEP e placas de carro.

def validar(placa):
    if placa == None or len(placa) <= 6:
        return "Quantidade de caracteres de placa é menos do que esperado."
    
    pattner = r'[A-Z][A-Z][A-Z]\-[0-9][0-9][0-9][0-9]'

    resultado = re.fullmatch(pattner, placa)
    if resultado == None:
        return "Placa do carro invalida."
    return f"Placa do carro valida -> {placa}"
