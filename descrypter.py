from cryptography.fernet import Fernet
import os


def descrypt_file():
    key = input("Enter the decryption key:")

    cipher = Fernet(key)

    arquivo_selecionado = input("Enter the path of the file to decrypt: ")

    with open(arquivo_selecionado, "rb") as arquivo:
        conteudo = arquivo.read()
        arquivo.close()

    conteudo_decriptado = cipher.decrypt(conteudo)

    os.remove(arquivo_selecionado)

    with open(arquivo_selecionado.replace(".encrypted", ""), "wb") as arquivo_decriptado:
        arquivo_decriptado.write(conteudo_decriptado)
        arquivo_decriptado.close()