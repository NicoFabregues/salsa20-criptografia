""" Implementación del algoritmo """
from PIL import Image


def salsa20_encrypt(key, nonce, counter, message):
    """ """
    pass


def encriptar_imagen(filename, key, nonce, counter):
    """ """
    image = Image.open(filename).convert('RGBA')
    image_bytes = bytes(image.tobytes())
    encrypted_image_bytes = salsa20_encrypt(key, nonce, counter, image_bytes)
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_image_bytes)
    encrypted_filename = "encrypted_" + filename
    encrypted_image.save(encrypted_filename)
    return encrypted_filename

def decrypt_image(filename, key, nonce, counter):
    """ """
    image = Image.open(filename).convert('RGBA')
    image_bytes = bytes(image.tobytes())
    decrypted_image_bytes = salsa20_encrypt(key, nonce, counter, image_bytes)
    decrypted_image = Image.frombytes(image.mode, image.size, decrypted_image_bytes)
    decrypted_filename = "decrypted_" + filename
    decrypted_image.save(decrypted_filename)
    return decrypted_filename


if __name__ == '__main__':
    print("\nAlgoritmo de encripción Salsa 20!\n")


