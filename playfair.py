key = "MONARCHY"

matrix = [
    ['M', 'O', 'N', 'A', 'R'],
    ['C', 'H', 'Y', 'B', 'D'],
    ['E', 'F', 'G', 'I', 'K'],
    ['L', 'P', 'Q', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Z']
]


def find(ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def encrypt(message):
    result = ""

    for i in range(0, len(message), 2):

        a = message[i]
        b = message[i + 1]

        r1, c1 = find(a)
        r2, c2 = find(b)

        # Same row
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]

        # Same column
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]

        # Rectangle
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


def decrypt(message):
    result = ""

    for i in range(0, len(message), 2):

        a = message[i]
        b = message[i + 1]

        r1, c1 = find(a)
        r2, c2 = find(b)

        # Same row
        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]

        # Same column
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]

        # Rectangle
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


message = input("Enter message: ").upper()
message = message.replace("J", "I")
message = message.replace(" ", "")

# Add X if message length is odd
if len(message) % 2 != 0:
    message += "X"

print("Original message:", message)

encrypted = encrypt(message)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted)
print("Decrypted message:", decrypted)
