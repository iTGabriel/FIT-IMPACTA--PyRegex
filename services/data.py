import re
# exemplos: datas, CPF, CEP e placas de carro.


def validar(data):
    if data == None or len(data) <= 6:
        return "Quantidade de caracteres de data é menos do que esperado."
    
    pattern1 = r'(0[0-9]|1[0-9]|2[0-9]|3[0-1])\/(0[0-9]|1[0-2])\/([0-2][0-9][0-9][0-9])' #dd/mm/aaaa
    pattern2 = r'(0[0-9]|1[0-9]|2[0-9]|3[0-1])\-(0[0-9]|1[0-2])\-([0-2][0-9][0-9][0-9])' #dd-mm-aaaa
    pattern3 = r'([0-2][0-9][0-9][0-9])\-(0[0-9]|1[0-2])\-(0[0-9]|1[0-9]|2[0-9]|3[0-1])' #aaaa-mm-dd
    pattern4 = r'(0[0-9]|1[0-9]|2[0-9]|3[0-1])([ ]de[ ])(janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)([ ]de[ ])([0-2][0-9][0-9][0-9])' #dd de mm...m de aaaa

    resultado1 = re.fullmatch(pattern1, data)
    resultado2 = re.fullmatch(pattern2, data)
    resultado3 = re.fullmatch(pattern3, data)
    resultado4 = re.fullmatch(pattern4, data)

    # print(f"{resultado1} - {resultado2} - {resultado3} - {resultado4} - {resultado5}")
    if resultado1 == None:
        if resultado2 == None:
            if resultado3 == None:
                if resultado4 == None:
                    return "INVALIDO"   
    return f"Data valida -> {data}"
