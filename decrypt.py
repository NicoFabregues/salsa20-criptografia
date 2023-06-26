from PIL import Image
from salsa20 import salsa20_encrypt
import argparse

def decrypt_image(filename, key, nonce, counter):
    """
    Esta función descifra una imagen cifrada utilizando Salsa20.
    Realiza el proceso inverso de encrypt_image. Abre la imagen cifrada,
    la convierte a bytes y luego descifra los bytes utilizando salsa20_encrypt.
    La imagen descifrada se guarda en un nuevo archivo.
    """
    image = Image.open(filename).convert("RGBA")
    image_bytes = bytes(image.tobytes())
    decrypted_image_bytes = salsa20_encrypt(key, nonce, counter, image_bytes)
    decrypted_image = Image.frombytes(image.mode, image.size, decrypted_image_bytes)
    decrypted_filename = "decrypted_" + filename
    decrypted_image.save(decrypted_filename)
    return decrypted_filename


def get_args():
    """Decrypt file"""
    arg_parser = argparse.ArgumentParser(
        prog="Salsa20 Decrypt File",
        epilog="File path",
    )
    arg_parser.add_argument(
        "-f",
        "--file",
        help="The file you want to decrypt",
    )
    return arg_parser.parse_args()


if __name__ == "__main__":
    print("\nAlgoritmo de descifrado Salsa 20!\n")

    # Clave, nonce, contador y nombre del archivo de imagen
    key = [0x80000000] * 8
    nonce = [0, 0]
    counter = 0
    args = get_args()
    # Descifrar la imagen cifrada y guardarla en un archivo
    decrypted_filename = decrypt_image(args.file, key, nonce, counter)
    print(f"Decrypted image saved as {decrypted_filename}")
