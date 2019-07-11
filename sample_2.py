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
    print("-- Hashing started --")
    # Tempo
    start_time = time.time()
    # The input message.
    collision_count = 0

    total_duration = 0

    file = open('dictionary.txt', 'r')

    for msg in file:
        # Delete \n at the end of string.
        msg = msg.rstrip()
        # Message in bytes.
        byte_str = msg.encode()
        # Hash object constructor, with hash length=3 bytes (24 bits).
        digest = blake2b(byte_str, digest_size=tamanho_hash)
        # Generate the message digest.
        hashed_msg = digest.hexdigest()

        if hashed_msg in hash_set:
            # Get collision time duration.
            duration = time.time() - start_time
            # print("Found a collision - word: {} -> hash: {} in {} seconds.".format(msg, hashed_msg, duration))
            # Empty the hash in every collision.
            hash_set = set()
            # Restart timer.
            start_time = time.time()
            collision_count += 1
            total_duration += duration

        if collision_count == tentativas:
            total_duration = total_duration / tentativas
            print("Collisions found: {}".format(tentativas))
            print("Average collision found time : {} seconds.".format(total_duration))
            return

        # Adds a new hash value to the set.
        hash_set.add(hashed_msg)

    if collision_count != 0:
        total_duration = total_duration / collision_count
        print("Collisions found: {}".format(collision_count))
        print("Average collision found time: {} seconds.".format(total_duration))

    else:
        print("No collisions found!")


# Generate a dictionary file. If it already exist, then only reads from it.
def gerar_dicionario():
    try:
        # Check if the dictionary file exist.
        file = open('dictionary.txt', 'r')
        print("Opening dictionary ...")
        file.close()
        return
    except IOError:
        print("Generating dictionary ...")

    file = open('dictionary.txt', 'w')

    # All possible combinations of n=tam_palavras letters.
    for i in product(ascii_letters, repeat=tam_palavras):
        file.write(''.join(i) + '\n')
    file.close()


if __name__ == '__main__':
    main()
