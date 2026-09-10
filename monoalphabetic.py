alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"


def encrypt(message):
    result = ""

    for ch in message:
        if ch.isalpha():
            ch = ch.upper()
            result += key[alphabet.index(ch)]
        else:
            result += ch

    return result


def decrypt(message):
    result = ""

    for ch in message:
        if ch.isalpha():
            ch = ch.upper()
            result += alphabet[key.index(ch)]
        else:
            result += ch

    return result


message = input("Enter message: ")

encrypted = encrypt(message)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted)
print("Decrypted message:", decrypted)
