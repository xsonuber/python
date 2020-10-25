import string
alphlow = list(string.ascii_lowercase)*2
alphup = list(string.ascii_uppercase)*2
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    keyw = ""
    while len(plaintext) > len(keyw):
        keyw += keyword

    key = []
    for i in range(len(keyw)):
        for j in range(26):
            if keyw[i] == alphlow[j] or keyw[i] == alphup[j]:
               key.append(j)

    for i in range(len(plaintext)):
        symb = ""
        for j in range(len(alphlow)//2):
            if plaintext[i] == alphlow[j]:
                symb = alphlow[j+key[i]]
            elif plaintext[i] == alphup[j]:
                symb = alphup[j+key[i]]
        if symb == "":
            symb = plaintext[i]
        ciphertext += symb
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    keyw = ""
    while len(ciphertext) > len(keyw):
        keyw += keyword

    key = []
    for i in range(len(keyw)):
        for j in range(26):
            if keyw[i] == alphlow[j] or keyw[i] == alphup[j]:
               key.append(j)

    for i in range(len(ciphertext)):
        symb = ""
        for j in range(len(alphlow)//2):
            if ciphertext[i] == alphlow[j]:
                symb = alphlow[j-key[i]]
            elif ciphertext[i] == alphup[j]:
                symb = alphup[j-key[i]]
        if symb == "":
            symb = ciphertext[i]
        plaintext += symb
    return plaintext
check = input('Если нужно зашифровать, введите "p", в другом случае введите "c": ')
text = input('Введите текст: ')
kw = input('Введите кодовое слово: ')
if check == 'p':
    print(encrypt_vigenere(text, kw))
elif check == 'c':
    print(decrypt_vigenere(text, kw))
