#-*- coding: UTF-8 -*-
import random

texto = "O Fulano de Tal é uma pessoa (legal, gente boa, simpatica) e (etc, etc)"
adjetivos = []
textoConverte = []
converteString = "".join(textoConverte)
linha = []

def converteTexto():
    global adjetivos
    global textoConverte
    x = 0

    for i in texto:
        if i == "(":
            add = i.split("<")
            x += 1
        
        if i == " ":
            leitorTexto = textoConverte.append(" ")

        if i == ", ":
            leitorTexto = textoConverte.append("")

        if i == ")":
            leitorTexto = textoConverte.append(x + ">")

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
print(textoConverte)
