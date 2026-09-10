def encrypt_once(message, key):
    result = ""

    # Arrange message in rows
    for i in range(len(key)):
        for j in range(i, len(message), len(key)):
            result += message[j]

    return result


def decrypt_once(message, key):
    columns = len(key)
    rows = (len(message) + columns - 1) // columns

    result = ""

    for i in range(rows):
        for j in range(columns):
            pos = j * rows + i

            if pos < len(message):
                result += message[pos]

    return result


message = input("Enter message: ").replace(" ", "")
key1 = input("Enter first key: ")
key2 = input("Enter second key: ")

# Encryption
step1 = encrypt_once(message, key1)
encrypted = encrypt_once(step1, key2)

print("Encrypted message:", encrypted)

# Decryption
step1 = decrypt_once(encrypted, key2)
decrypted = decrypt_once(step1, key1)

print("Decrypted message:", decrypted)
