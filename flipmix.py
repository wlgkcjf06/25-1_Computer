import encryptor as en
import decryptor as de


def main():
    opt = input("Encrypt or Decrypt? (e/d): ").lower()
    if opt == 'e':
        message = input("Enter the message to encrypt: ")
        encrypted_message = en.encrypt(message)
        print("Encrypted message:", encrypted_message)
    elif opt == 'd':
        message = input("Enter the message to decrypt: ")
        decrypted_message = de.decrypt(message)
        print("Decrypted message:", decrypted_message)

main()