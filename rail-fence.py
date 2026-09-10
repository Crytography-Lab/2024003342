def encrypt(message, key):
    rails = [""] * key
    row = 0
    direction = 1

    for ch in message:
        rails[row] += ch

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return "".join(rails)


def decrypt(cipher, key):
    pattern = []
    row = 0
    direction = 1

    for i in range(len(cipher)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    result = [""] * len(cipher)
    index = 0

    for r in range(key):
        for i in range(len(cipher)):
            if pattern[i] == r:
                result[i] = cipher[index]
                index += 1

    return "".join(result)


message = input("Enter message: ")
key = int(input("Enter number of rails: "))

encrypted = encrypt(message, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted message:", decrypted)
