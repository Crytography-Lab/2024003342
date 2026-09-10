def encrypt(message, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in message:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch.upper()) - 65 + shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result


def decrypt(message, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in message:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch.upper()) - 65 - shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result


message = input("Enter message: ")
key = input("Enter key: ")

encrypted = encrypt(message, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted message:", decrypted)
