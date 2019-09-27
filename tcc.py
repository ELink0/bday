# -*- coding: UTF-8 -*-
texto = "O Fulano de Tal é uma pessoa (legal, gente boa, simpatica) e (etc, etc)"
adjetivos = []
#ajetivos = [[0, 0, 0], [0, 0, 0]]

def identificaParenteses():
    global adjetivos

    adjetivo = ""
    estado = "fora"


    for t in texto:
        linha = [] # cria uma linha para a matriz
        quant_linhas = len(adjetivos)

        if estado == "fora":
            if t == "(":
                estado = "dentro"
                adjetivo = ""

        elif estado == "dentro":
            if t == ")":
                adjetivos.append(adjetivo)
                adjetivos.append(linha)
                estado = "fora"
                

            elif t == ",":
                adjetivos.append(adjetivo)
                adjetivo = ""

            else:
                adjetivo += t


identificaParenteses()
print(adjetivos)
