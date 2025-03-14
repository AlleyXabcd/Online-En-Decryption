def caesar_cipher_encrypt(text, key):
    shift = int(key)
    encrypted_text = "".join(
        [chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 + shift) % 26 + 65) for char
         in text])

    return encrypted_text


def caesar_cipher_decrypt(text, key):
    shift = int(key)
    decrypted_text = "".join(
        [chr((ord(char) - 97 - shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 - shift) % 26 + 65) for char
         in text])
    return decrypted_text