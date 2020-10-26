def is_prime(n: int) -> bool:
    i = 2
    check = 0
    while i < n:
        if n % i == 0:
            check += 1
        i += 1
    if check == 0 and n != 0:
        return True
    else:
        return False

def gcd(a: int, b:int) -> int:
    while a != 0 and b != 0:
        x = max(a, b)
        y = min(a, b)
        if x % y == 0:
            return y
            break
        else:
            if a == max(a, b):
                a = x % y
            else:
                b = x % y

def multiplicative_inverse(e: int, phi: int) -> int:
    div = []
    a, b = phi, e
    mod = 1
    while mod != 0:
        mod = a % b
        div.append(a//b)
        a, b = b, mod
    x = [0]*(len(div))
    y = [0]*(len(div))
    div = div[::-1]
    y[0] = 1
    for i in range(1, len(div)):
        x[i] = y[i-1]
        y[i] = x[i-1] - y[i-1]*div[i]
    return y[len(div)-1] % phi


def generate_keypair(p: int, q: int): #-> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q
    phi = (p-1)*(q-1)
    import random
    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

pp, qq = map(int, input('Введите два простых числа "p" и "q" через пробел: ').split())
print(generate_keypair(pp, qq))
