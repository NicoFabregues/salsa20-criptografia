import struct


def quarter_round(a, b, c, d):
    """
    Esta función realiza una operación de cuarto de ronda en los valores a, b, c y d.
    Es una operación básica utilizada en el algoritmo Salsa20.
    """
    a += b
    d ^= a
    d = (d << 16) | (d >> 16)
    c += d
    b ^= c
    b = (b << 12) | (b >> 20)
    a += b
    d ^= a
    d = (d << 8) | (d >> 24)
    c += d
    b ^= c
    b = (b << 7) | (b >> 25)
    return a, b, c, d


def salsa20_word_specification(state):
    """
    Realiza múltiples rondas de operaciones de cuarto de ronda
    en el estado para generar una secuencia de palabras.
    """
    x = list(state)
    for _ in range(10):
        x[4], x[0], x[12], x[8] = quarter_round(x[4], x[0], x[12], x[8])
        x[9], x[5], x[1], x[13] = quarter_round(x[9], x[5], x[1], x[13])
        x[14], x[10], x[6], x[2] = quarter_round(x[14], x[10], x[6], x[2])
        x[3], x[15], x[11], x[7] = quarter_round(x[3], x[15], x[11], x[7])
        x[1], x[0], x[3], x[2] = quarter_round(x[1], x[0], x[3], x[2])
        x[6], x[5], x[4], x[7] = quarter_round(x[6], x[5], x[4], x[7])
        x[11], x[10], x[9], x[8] = quarter_round(x[11], x[10], x[9], x[8])
        x[12], x[15], x[14], x[13] = quarter_round(x[12], x[15], x[14], x[13])
    return [(a + b) & 0xffffffff for a, b in zip(x, state)]


def salsa20_8(state):
    """
    Esta función toma el resultado de salsa20_word_specification
    y lo empaqueta en una cadena de bytes de longitud 8.
    """
    return b''.join(struct.pack('<I', x) for x in salsa20_word_specification(state))


def salsa20_key_schedule(key, nonce, counter):
    """
    Esta función genera el programa de clave de Salsa20.
    Combina la clave, el nonce y el contador en una secuencia
    que se utilizará para generar la secuencia de clave.
    """
    key_constants = (0x61707865, 0x3320646e, 0x79622d32, 0x6b206574)
    key_stream = list(key_constants)
    key_stream.extend(key)
    key_stream.append(counter)
    key_stream.extend(nonce)
    key_stream.extend(key_constants[1:])
    return key_stream


def salsa20_encrypt(key, nonce, counter, message):
    """
    Esta función cifra un mensaje utilizando Salsa20.
    Divide el mensaje en bloques de 64 bytes y para cada bloque,
    genera la secuencia de clave correspondiente utilizando el programa de clave
    y realiza una operación XOR entre el bloque del mensaje y la secuencia de clave.
    """
    encrypted_message = b""
    for i in range(0, len(message), 64):
        block = message[i: i + 64]
        key_stream = salsa20_8(salsa20_key_schedule(key, nonce, counter + (i // 64)))
        encrypted_block = bytes(m ^ k for m, k in zip(block, key_stream))
        encrypted_message += encrypted_block
    return encrypted_message
