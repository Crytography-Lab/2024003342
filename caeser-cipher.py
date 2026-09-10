def caesar_encrypt(text, key):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            result += char

    return result


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)


# Main program
text = input("Enter the message: ")
key = int(input("Enter the key: "))

encrypted = caesar_encrypt(text, key)
decrypted = caesar_decrypt(encrypted, key)

print("\nEncrypted message:", encrypted)
print("Decrypted message:", decrypted)
