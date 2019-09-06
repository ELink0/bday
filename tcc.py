# -*- coding: UTF-8 -*-
texto = "O Fulano de Tal é uma pessoa (legal, gente boa, simpatica) e (etc, etc)"
adjetivos = []

def identificaParenteses():
    # Máquina de estado -> Automato Finito Deterministico (estudar mais)
    # Olhar Hierarquia de Chomsky, gramática regular e expressão regular
    global adjetivos
    adjetivo = ""
    estado = "fora"
    for t in texto:
        if estado == "fora":
            if t == "(":
                estado = "dentro"
                adjetivo = ""
        elif estado == "dentro":
            if t == ")":
                adjetivos.append(adjetivo)
                estado = "fora"
            elif t == ",":
                adjetivos.append(adjetivo)
                adjetivo = ""
            else:
                adjetivo += t

# 2 - Separar as vírgulas em uma matriz, o adjetivo zero vai ser uma lista diferente
# 3 - Explicar o ataque do aniversário (ESTUDAR SUMÁRIO DE MENSAGEM, VER NO TANEMBAL LIVRO DE REDES, CAPT. SEGURANÇA)
identificaParenteses()
print(adjetivos)
