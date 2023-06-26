from PIL import Image
from salsa20 import salsa20_encrypt
import argparse


def encrypt_image(filename, key, nonce, counter):
    """
    Esta función cifra una imagen utilizando Salsa20.
    Abre la imagen, la convierte a bytes y luego cifra los bytes de la imagen
    utilizando salsa20_encrypt. La imagen cifrada se guarda en un nuevo archivo.
    """
    image = Image.open(filename).convert("RGBA")
    image_bytes = bytes(image.tobytes())
    encrypted_image_bytes = salsa20_encrypt(key, nonce, counter, image_bytes)
    encrypted_image = Image.frombytes(image.mode, image.size, encrypted_image_bytes)
    encrypted_filename = "encrypted_" + filename
    encrypted_image.save(encrypted_filename)
    return encrypted_filename


def get_args():
    """Encrypt file"""
    arg_parser = argparse.ArgumentParser(
        prog="Salsa20 Encrypt File",
        epilog="File path",
    )
    arg_parser.add_argument(
        "-f",
        "--file",
        help="The file you want to encrypt",
    )
    return arg_parser.parse_args()


if __name__ == "__main__":
    print("\nAlgoritmo de encripción Salsa 20!\n")

    # Clave, nonce, contador y nombre del archivo de imagen
    key = [0x80000000] * 8
    nonce = [0, 0]
    counter = 0
    args = get_args()
    # Cifrar la imagen y guardarla en un archivo
    encrypted_filename = encrypt_image(args.file, key, nonce, counter)
    print(f"Encrypted image saved as {encrypted_filename}")
