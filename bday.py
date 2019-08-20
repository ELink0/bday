1 - Identificar Parenteses dentro de uma string

def IdentificaParenteses();
    palavras = []
    texto = ("O João é (legal, gente boa)")
    
    for i in texto:
        if i == ("()"):
            palavras.append(i)
