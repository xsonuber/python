import string
alphlow = list(string.ascii_lowercase)*2
alphup = list(string.ascii_uppercase)*2
def decrypt_caesar(ciphertext: str, shift: int) -> str:
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
def caesar_breaker(ciphertext: str, dictionary) -> int:
    best_shift = 0
    word = ""
    while decrypt_caesar(ciphertext, best_shift) != word:
        if best_shift == 52:
            return "Error"
            break
        for i in dictionary:
            if decrypt_caesar(ciphertext, best_shift) == i:
                word = i
        best_shift += 1
    best_shift -= 26
    return best_shift
d = {} #у меня не получилось организовать ввод словаря с клавиатуры
text = input("Введите зашифрованный текст: ")
print(caesar_breaker(text, d))
