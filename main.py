import descrypter
import encrypter

def main():

    menu_option = input("Select an option:\n[1] - Encrypt a file\n[2] - Decrypt a file\n[0] - Exit\nOption: ")

    match menu_option:
        case "1":
            encrypter.encrypt_file()

        case "2":
            descrypter.descrypt_file()

        case "0":
            exit()


if __name__ == "__main__":
    main()