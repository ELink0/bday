vetorInt = [10, 20, 30, 40]

def SomaVetorInterior(v):
    soma = 0
    for i in v:
        soma += i
    return soma

def SomaVetorInteriorRec_(v, i):
    if i < len(v):
        return SomaVetorInteriorRec_(v, i+1) + v[i]
    else:
        return 0

def SomaVetorInteriorRec(v):
    return SomaVetorInteriorRec_(v, 0)



resultado = SomaVetorInterior(vetorInt)
print(resultado)

resultado2 = SomaVetorInteriorRec(vetorInt)
print(resultado2)
