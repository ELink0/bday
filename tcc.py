#-*- coding: UTF-8 -*-
texto = "O Fulano de Tal é uma pessoa (legal, gente boa, simpatica) e (etc, etc)"
adjetivos = []
textoConverte = "O Fulano de Tal é uma pessoa <t0>, mas, também é <t1>, sendo assim, eu considero ela como sendo muito <t2>. Eu <t3> essa pessoa."
linha = [] # cria uma linha para a matriz


def converteTexto():
    estado = "fora"
    x = 0
    for i in textoConverte:
        if estado == "fora":
            if i == "<":
                estado = "dentro"
                
        elif estado == "dentro":
          if i == ">":
            converter = i.replace(i, textoConverte[x])
            x += 1

def identificaParenteses():
    global adjetivos
    global linha

    adjetivo = ""
    estado = "fora"


    for t in texto:
        
        quant_linhas = len(adjetivos)

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
                linha.append(adjetivos)
                adjetivo = ""

            else:
                adjetivo += t
                


identificaParenteses()
converteTexto()
print(textoConverte)
