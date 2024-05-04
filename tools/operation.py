from sympy import factorint


def euclidean_extended_algorithm(a, b):
    """
    标准欧几里得扩展算法
    返回一个元组(g, x, y),使得 a*x + b*y = g = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = euclidean_extended_algorithm(b, a % b)
        return g, x - (a // b) * y, y


def modular_exponentiation(a, c, b=None):
    """
    计算 a^b % c

    参数:
    a (int): 底数
    b (int): 指数(可选)
    c (int): 取模数

    返回:
    int: a^b % c 的结果
    """
    if b is None:
        return a % c

    result = 1
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        b //= 2
    return result


def gcd(a, b):
    """
    计算两个整数的最大公约数
    """
    while b != 0:
        a, b = b, a % b
    return a


def modinv(a, m):
    """
    计算 a 关于模 m 的乘法逆元
    """
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def prime_factors(n):
    """ 使用 SymPy 的 factorint 函数进行素数分解。
        返回一个字典，键是素数因子，值是对应的指数。
    """
    return factorint(n)

def or_1(a, b):
    return a ^ b
def operation_m():
    while True:
        print('''
=========================================================
operation
1:BEEA
标准欧几里得扩展算法接受(a,b)返回(g，x，y)使得a*x+b*y=g=φ(a，b)
2:MOD
计算 a^b % c(不提供b则为a mod c）
3:TMAXcd
计算两个数最大公约数
4:modinv
计算 a 关于模 m 的乘法逆元
5:PF
尝试素数分解n--> p q
6:or
ret=a ^ b
=========================================================
''')
        choice = int(input('-->'))
        if choice == 1:
            a1 = int(input('a->'))
            b1 = int(input('b->'))
            print('[INFO]' + str(euclidean_extended_algorithm(a1, b1)))
        if choice == 2:
            a1 = int(input('a->'))
            b1 = int(input('b->'))
            c1 = int(input('c->'))
            if b1 == 3:
                print('[INFO]' + str(modular_exponentiation(a1, c1)))
            else:
                print('[INFO]' + str(modular_exponentiation(a1, c1, b1)))
        if choice == 4:
            a1 = int(input('a->'))
            b1 = int(input('b->'))
            print('[INFO]' + str(gcd(a1, b1)))
        if choice == 5:
            a1 = int(input('-->'))
            print('[INFO]' + str(prime_factors(a1)))
        if choice == 6:
            print(or_1(int(input('a->')), int(input('b->'))))
        else:
            return
