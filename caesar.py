import string
alphlow = list(string.ascii_lowercase)*2
alphup = list(string.ascii_uppercase)*2
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in range(len(plaintext)):
        symb = ""
        for j in range(len(alphlow)//2):
            if plaintext[i] == alphlow[j]:
                symb = alphlow[j+shift]
            elif plaintext[i] == alphup[j]:
                symb = alphup[j+shift]
        if symb == "":
            symb = plaintext[i]
        ciphertext += symb
    return ciphertext
def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in range(len(ciphertext)):
        symb = ""
        for j in range(len(alphlow)//2):
            if ciphertext[i] == alphlow[j]:
                symb = alphlow[j-shift]
            elif ciphertext[i] == alphup[j]:
                symb = alphup[j-shift]
        if symb == "":
            symb = ciphertext[i]
        plaintext += symb
    return plaintext
check = input('Если нужно зашифровать, введите "p", в другом случае введите "c": ')
text = input('Введите текст: ')
sh = int(input('Введите шаг: '))
if check == 'p':
    print(encrypt_caesar(text, sh))
elif check == 'c':
    print(decrypt_caesar(text, sh))
