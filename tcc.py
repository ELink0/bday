# -*- coding: UTF-8 -*-
texto = "O Fulano de Tal é uma pessoa (legal, gente boa, simpatica) e (etc, etc)"
adjetivos = []

def identificaParenteses():
    global adjetivos

    adjetivo = ""
    estado = "fora"
    n_lista = 0

    for t in texto:
        if estado == "fora":
            if t == "(":
                estado = "dentro"
                adjetivo = ""

        elif estado == "dentro":
            if t == ")":
                adjetivos.append(adjetivo)
                n_lista += 1
                estado = "fora"
                adjetivos.append(adjetivos)

            elif t == ",":
                adjetivos.append(adjetivo)
                adjetivo = ""

            else:
                adjetivo += t

identificaParenteses()
print(adjetivos)
