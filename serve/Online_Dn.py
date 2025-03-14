from flask import Flask, request, jsonify
from flask_cors import CORS
from caesar import caesar_cipher_encrypt,caesar_cipher_decrypt
from vigenere import vigenere_cipher_encrypt,vigenere_cipher_decrypt
from RC4 import rc4_encrypt,rc4_decrypt

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])
@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    algorithm = data.get('algorithm')
    text = data.get('text')
    key = data.get('key')

    if algorithm == 'Caesar cipher':
        result = caesar_cipher_encrypt(text, key)
    elif algorithm == 'Vigenere Cipher':
        result = vigenere_cipher_encrypt(text, key)
    elif algorithm == 'RC4':
        result = rc4_encrypt(text, key)
    else:
        return jsonify({"error": "Unsupported algorithm"}), 400

    return jsonify({"result": result})

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    algorithm = data.get('algorithm')
    text = data.get('text')
    key = data.get('key')

    if algorithm == 'Caesar cipher':
        result = caesar_cipher_decrypt(text, key)
    elif algorithm == 'Vigenere Cipher':
        result = vigenere_cipher_decrypt(text, key)
    elif algorithm == 'RC4':
        result = rc4_decrypt(text, key)
    else:
        return jsonify({"error": "Unsupported algorithm"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True, port=8000)