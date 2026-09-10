def encrypt(message, key):
    result = ""

    for i in range(0, len(message), 2):
        x = ord(message[i]) - 65
        y = ord(message[i + 1]) - 65

        a = (key[0][0] * x + key[0][1] * y) % 26
        b = (key[1][0] * x + key[1][1] * y) % 26

        result += chr(a + 65)
        result += chr(b + 65)

    return result


def decrypt(message, inverse_key):
    result = ""

    for i in range(0, len(message), 2):
        x = ord(message[i]) - 65
        y = ord(message[i + 1]) - 65

        a = (inverse_key[0][0] * x +
             inverse_key[0][1] * y) % 26

        b = (inverse_key[1][0] * x +
             inverse_key[1][1] * y) % 26

        result += chr(a + 65)
        result += chr(b + 65)

    return result


# Key matrix
key = [
    [3, 3],
    [2, 5]
]

# Inverse key matrix
inverse_key = [
    [15, 17],
    [20, 9]
]

message = input("Enter message: ").upper()
message = message.replace(" ", "")

# Add X if message length is odd
if len(message) % 2 != 0:
    message += "X"

encrypted = encrypt(message, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, inverse_key)
print("Decrypted message:", decrypted)
