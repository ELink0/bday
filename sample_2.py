from hashlib import blake2b
from itertools import product
from string import ascii_letters
import time

# Tamanho da hash em bytes
tamanho_hash = 3

# Número de tentativas
tentativas = 100

# Número de letras por palavra
tam_palavras = 3


def main():
    gerar_dicionario()
    # Usar o set para aprimorar a velocidade
    hash_set = set()
    print("-- Colisões Hashing iniciadas --")
    # Tempo
    inicio_tempo = time.time()
    # Mensagem
    contador_colisoes = 0

    duracao_total = 0

    arquivo = open('dictionary.txt', 'r')

    for msg in arquivo:
        # Deleta o \n no final da string.
        msg = msg.rstrip()
        # Messagem em bytes
        byte_str = msg.encode()
        # Construtor de objeto hash, com hash lenght=3 bytes (24 bits)
        digest = blake2b(byte_str, digest_size=tamanho_hash)
        # Generate the message digest.
        hashed_msg = digest.hexdigest()

        if hashed_msg in hash_set:
            # Pegar a duração das colisões
            duration = time.time() - inicio_tempo
            # print("Found a collision - word: {} -> hash: {} in {} seconds.".format(msg, hashed_msg, duration))
            # Limpa a hash a cada colisão
            hash_set = set()
            # Reincia o timer
            inicio_tempo = time.time()
            contador_colisoes += 1
            duracao_total += duration

        if contador_colisoes == tentativas:
            duracao_total = duracao_total / tentativas
            print("Collisions found: {}".format(tentativas))
            print("Average collision found time : {} seconds.".format(duracao_total))
            return

        # Add um novo valor hash para setar
        hash_set.add(hashed_msg)

    if contador_colisoes != 0:
        duracao_total = duracao_total / contador_colisoes
        print("Colisões encontradas: {}".format(contador_colisoes))
        print("Tempo estimado das colisões: {} segundos.".format(duracao_total))

    else:
        print("Nenhuma colisão encontrada!")


# Gera um arquivo dicionário. Se já existir, ele apenas lê.
def gerar_dicionario():
    try:
        # Verificar se o arquivo existe.
        arquivo = open('dictionary.txt', 'r')
        print("Abrindo dicionário ...")
        arquivo.close()
        return
    except IOError:
        print("Gerando dicionário ...")

    arquivo = open('dictionary.txt', 'w')

    # Todas as combinações possível de n=tam_palavras.
    for i in product(ascii_letters, repeat=tam_palavras):
        arquivo.write(''.join(i) + '\n')
    arquivo.close()


if __name__ == '__main__':
    main()
