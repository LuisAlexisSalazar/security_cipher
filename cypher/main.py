import numpy as np
import random
from sympy import Matrix

encrypt_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                      'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                      'X': 23, 'Y': 24, 'Z': 25,
                      '0': 26, '1': 27, '2': 28, '3': 29, '4': 30, '5': 31, '6': 32, '7': 33, '8': 34, '9': 35, '.': 36,
                      ',': 37, ':': 38, '?': 39, ' ': 40}

decrypt_dictionary = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I',
                      '9': 'J', '10': 'K', '11': 'L', '12': 'M',
                      '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U',
                      '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': '0',
                      '27': '1', '28': '2', '29': '3', '30': '4', '31': '5', '32': '6', '33': '7', '34': '8',
                      '35': '9', '36': '.', '37': ',', '38': ':', '39': '?', '40': ' '}


def getKey(size):
    """
    :size: matrix size
    :return: size x size matrix containing the key
    """

    matrix = []
    L = []

    # fill list with amount of size*size elements
    for x in range(size * size):
        L.append(random.randrange(40))

    # list to matrix size * size
    matrix = np.array(L).reshape(size, size)

    return matrix


def cipher(message, key):
    """
    :message: message to cipher (plaintext)
    :return: ciphered text
    """

    cipher_text = ''

    # Variables
    matrix_message = []
    list_temp = []
    cifrado_final = ''
    temp_cipher_text = ''
    cont = 0

    # Cast Capital Letter
    message = message.upper()

    if len(message) <= len(key):
        # Fill with 'X' until == key
        while len(message) < len(key):
            message = message + 'X'

        # Create matrix to cipher
        for i in range(0, len(message)):
            matrix_message.append(encrypt_dictionary[message[i]])

        matrix_message = np.array(matrix_message)

        # Multiply matrix and message
        matrix_cipher_number = np.matmul(key, matrix_message)

        # Module
        matrix_cipher_number = matrix_cipher_number % 41

        # Generate Cipher Text
        for i in range(0, len(matrix_cipher_number)):
            cipher_text += decrypt_dictionary[str(matrix_cipher_number[i])]
    else:
        # Add 'X' to be divisible by key size
        while len(message) % len(key) != 0:
            message = message + 'X'

        # The message is dividing in substring of len(key)
        matrix_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]

        for block in matrix_message:
            # Create matrix to the block
            for i in range(0, len(block)):
                list_temp.append(encrypt_dictionary[block[i]])

            matrix_encrypt = np.array(list_temp)

            # Multiply matrix and message block 
            matrix_cipher_number = np.matmul(key, matrix_encrypt)

            # Se obtiene el modulo sobre el diccionario de cada celda

            matrix_cipher_number = matrix_cipher_number % 41

            # Se codifica de valores numericos a los del diccionario, añadiendo a ciphertext el valor en el diccionario pasandole como indice la i posicion de la variable cifrado

            for i in range(0, len(matrix_cipher_number)):
                temp_cipher_text += decrypt_dictionary[str(matrix_cipher_number[i])]

            # Se inicializan las variables para el nuevo block

            matrix_encrypt = []
            list_temp = []

        # Se añade el mensaje encriptado a la variable que contiene el mensaje encriptado completo

        cipher_text = temp_cipher_text

    # --------------------------------

    return cipher_text


def decipher(message, key):
    """
    :message: message to decipher (ciphertext)
    :return: plaintext deciphered
    """
    plaintext = ''

    matrix_message = []
    temp_plain_text = ''
    list_temp = []
    inverse_matrix = []
    matrix_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]

    inverse_matrix = Matrix(key).inv_mod(41)
    inverse_matrix = np.array(inverse_matrix)

    inverse_matrix = inverse_matrix.astype(float)

    # to each block
    for block in matrix_message:

        for i in range(0, len(block)):
            list_temp.append(encrypt_dictionary[block[i]])

        matrix_encrypt = np.array(list_temp)

        cifrado = np.matmul(inverse_matrix, matrix_encrypt)

        cifrado = np.remainder(cifrado, 41).flatten()

        # Decipher
        for i in range(0, len(cifrado)):
            temp_plain_text += decrypt_dictionary[str(int(cifrado[i]))]

        matrix_encrypt = []
        list_temp = []
    plaintext = temp_plain_text

    # Delete filling of 'X'

    while plaintext[-1] == 'X':
        plaintext = plaintext.rstrip(plaintext[-1])

    return plaintext


if __name__ == '__main__':
    key = getKey(10)
    print("Key:\n", key)
    plaintext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse commodo nisi nec mauris dignissim, id " \
                "vestibulum dolor aliquam. Aenean eget elit eu mauris ultricies ultricies. Curabitur rhoncus venenatis quam eget dictum. Aliquam pellentesque, " \
                "nulla non faucibus hendrerit, turpis justo ornare lectus, iaculis porta ipsum ligula vitae mi. Nam tincidunt fermentum ligula, vitae varius dolor molestie in. " \
                "Pellentesque finibus facilisis consequat. Sed at ante viverra, sagittis velit vel, tincidunt justo. Pellentesque elit tellus, porttitor ac sapien nec, " \
                "mollis scelerisque diam."
    print("Texto de Entrada:\n", plaintext)
    cipherText = cipher(plaintext, key)
    print("Texto Cifrado:\n", cipherText)
    decipherText = decipher(cipherText, key)
    print("Texto Descifrado:\n", decipherText)
