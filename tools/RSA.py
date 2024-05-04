from sympy import Rational, continued_fraction, continued_fraction_convergents
from tools.yafu.yafu import *
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

def p_q_e_to_d(p, q, e):
    """
    计算 RSA 私钥 d
    """
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    return d


def rsa_decrypt(p, q, e, c):
    """
    RSA 解密函数

    参数:
    p (int): 素数 p
    q (int): 素数 q
    e (int): 公钥指数 e
    c (int): 密文 c

    返回:
    int: 解密后的明文 m
    """
    # 计算 n = p * q
    n = p * q

    # 计算 phi(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)

    # 计算私钥指数 d
    # 使用扩展欧几里得算法计算 d = e^-1 (mod phi(n))
    d = pow(e, -1, phi)

    # 使用私钥 d 解密密文 c
    m = pow(c, d, n)

    return m


def p_q_dp_dq_c_to_m(p, q, dp, dq, c):
    """使用中国剩余定理和给定的p, q, dp, dq解密RSA密文c"""
    # 计算模数n
    n = p * q

    # 计算密文c在p和q下的幂
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)

    # 计算q的模p逆元
    q_inv = modinv(q, p)

    # 使用中国剩余定理合并结果
    h = (q_inv * (m1 - m2)) % p
    m = (m2 + h * q) % n

    return m


def e_n_dp_c_to_m(e, n, dp, c):
    def modular_inverse(e1, phi1):
        """ 使用扩展欧几里得算法来计算模逆 """
        d_1, x1, x2, y1 = 0, 0, 1, 1
        temp_phi = phi1

        while e1 > 0:
            temp1 = temp_phi // e1
            temp2 = temp_phi - temp1 * e1
            temp_phi, e1 = e1, temp2

            x = x2 - temp1 * x1
            y = d_1 - temp1 * y1

            x2, x1 = x1, x
            d_1, y1 = y1, y

        if temp_phi == 1:
            return d_1 + phi1
        return 0  # 如果不存在模逆，返回0（不应该发生在RSA中）

    # 尝试找到合适的 p 和 q
    for i in range(1, e):
        if (dp * e - 1) % i == 0:
            p = ((dp * e - 1) // i) + 1
            if n % p == 0:  # 确保 p 是 n 的一个因子
                q = n // p
                phi = (p - 1) * (q - 1)  # 计算欧拉函数 φ(n)
                d = modular_inverse(e, phi)  # 计算 e 关于 φ(n) 的模逆
                if d == 0:
                    continue  # 如果没有找到有效的模逆，跳过当前循环
                m = pow(c, d, n)  # 使用模幂运算解密
                return m
    return None  # 如果没有找到合适的 p 和 q，返回 None

def small_d(e, n):
    frac = Rational(e, n)
    # 获取连分数展开
    cf = continued_fraction(frac)
    # 生成收敛值
    convergents = continued_fraction_convergents(cf)

    for conv in convergents:
        k, d = conv.numerator, conv.denominator
        # 检查该d是否是私钥d的可能值
        if pow(pow(2, e, n), d, n) == 2:
            return f"Possible d: {d}"
    return "No valid d found."

def decrypt_rsa(c, d, n):
    # 解密密文 c
    m = pow(c, d, n)
    return m


def n_c_e_to_m(n, c, e):
    factors = yafu_get(str(n) + '\n\n')  # 将参数转换为字符串类型

    # 计算 phi
    phi = 1
    for factor in factors:
        phi *= factor - 1

    # 计算 d
    d = modinv(e, phi)

    # 解密消息
    m_hex = hex(pow(c, d, n))[2:]
    m_bytes = bytes.fromhex(m_hex)

    return m_bytes.decode('utf-8')

def rsam():
    while True:
        print('''
===================
RSA TOOLS
1:p q e -> d
2:p q e c -> m
3:p q dp dq c-> m
4:e n dp c -> m
5:small d
  e n -> d
6:c d n -> m
7:n=small * x
m c e -> m
======================
''')
        choice = int(input('-->'))
        if choice == 0:
            print(hex(int(input('-->'))))
        if choice == 1:
            p1 = int(input('p-->'))
            q1 = int(input('q-->'))
            e1 = int(input('e-->'))
            print('[INFO]' + str(p_q_e_to_d(p1, q1, e1)))
        if choice == 2:
            p1 = int(input('p-->'))
            q1 = int(input('q-->'))
            e1 = int(input('e-->'))
            c1 = int(input('c-->'))
            print('[INFO]' + str(rsa_decrypt(p1, q1, e1, c1)))
        if choice == 3:
            p1 = int(input('p-->'))
            q1 = int(input('q-->'))
            dp1 = int(input('dp-->'))
            dq1 = int(input('dq-->'))
            c1 = int(input('c-->'))
            print('[INFO]' + str(p_q_dp_dq_c_to_m(p1, q1, dp1, dq1, c1)))
        if choice == 4:
            e1 = int(input('e-->'))
            n1 = int(input('n-->'))
            dp1 = int(input('dp-->'))
            c1 = int(input('c-->'))
            print('[INFO]' + str(e_n_dp_c_to_m(e1, n1, dp1, c1)))
        if choice == 5:
            e1 = int(input('e-->'))
            n1 = int(input('n-->'))
            print('[INFO]' + str(small_d(e1, n1)))
        if choice == 6:
            c1 = int(input('c-->'))
            d1 = int(input('d-->'))
            n1 = int(input('n-->'))
            print('[INFO]' + str(decrypt_rsa(c1, d1, n1)))
        if choice == 7:
            n1 = int(input('n-->'))
            c1 = int(input('c-->'))
            e1 = int(input('e-->'))
            print('[INFO]' + str(n_c_e_to_m(n1, c1, e1)))
        else:
            return
