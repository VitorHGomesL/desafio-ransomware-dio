from cryptography.fernet import Fernet
import os

def encrypt_file():

    arquivo_selecionado = input("Enter the path of the file to encrypt: ")

    key = Fernet.generate_key()

    print('''

ATTENTION: THIS IS THE GENERATED ENCRYPTION KEY FOR YOUR FILE, IF YOU LOSE THIS KEY, YOU WILL NOT BE ABLE TO DECRYPT YOUR FILE!!!
      
PLEASE SAVE THIS KEY IN A SAFE PLACE AND DO NOT SHARE IT WITH ANYONE.
      
GENERATED KEY:

''', key.decode(), 

'''
BE SURE TO COPY AND SAVE THIS KEY IN A SAFE PLACE. IF YOU LOSE THIS KEY, YOU WILL NOT BE ABLE TO DECRYPT YOUR FILE!!!!
''')

    cipher = Fernet(key)

    with open(arquivo_selecionado, "rb") as arquivo:
        conteudo = arquivo.read()
        arquivo.close()

    os.remove(arquivo_selecionado)

    conteudo_encriptado = cipher.encrypt(conteudo)

    with open(arquivo_selecionado + ".encrypted", "wb") as arquivo_encriptado:
        arquivo_encriptado.write(conteudo_encriptado)
        arquivo_encriptado.close()