import base64

def KSA(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]


def RC4(key, text):
    S = KSA(key)
    keystream = PRGA(S)
    return bytes([c ^ next(keystream) for c in text])


def rc4_encrypt(text, key):
    key = [ord(c) for c in key]
    text = text.encode('utf-8')
    encrypted = RC4(key, text)
    return base64.b64encode(encrypted).decode('utf-8')


def rc4_decrypt(encrypted, key):
    key = [ord(c) for c in key]
    encrypted = base64.b64decode(encrypted)
    decrypted = RC4(key, encrypted)
    return decrypted.decode('utf-8')