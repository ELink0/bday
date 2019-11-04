#-*- coding: UTF-8 -*-
import random

texto = "O Fulano de Tal é uma pessoa (legal, gente boa, simpatica) e (etc, etc). Ele também é muito (trabalhador, criativo, educado) faz parte de uma família (muito boa, excelente, renomada)"
adjetivos = []
textoConverte = []
linha = []

def converteTexto():
    global adjetivos
    global textoConverte
    x = 0

    for i in texto:
        if i == "(":
            leitorTexto = textoConverte.append("<")
            leitorTexto = textoConverte.append("t")
            x += 1

        if i == ", ":
            leitorTexto = textoConverte.append("")

        if i == ")":
            leitorTexto = textoConverte.append(">")
            x = 0

        if x > 0:
            x =+ 1
        
        else:
            leitorTexto = textoConverte.append(i)

def identificaParenteses():
    global adjetivos
    global linha

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
                adjetivos.append(linha)
                adjetivo = ""

            else:
                adjetivo += t


converteTexto()
print(''.join(textoConverte).replace("'", ""))
