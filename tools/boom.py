def caesar_1(ciphertext, alphabet):
    """ 对给定的密文进行凯撒密码的暴力破解，尝试每一种可能的移位，并打印结果。 """
    ciphertext = ciphertext.upper()  # 将密文转换为大写以简化处理

    # 尝试所有的可能移位
    for key in range(26):
        plaintext = ''
        for char in ciphertext:
            if char in alphabet:
                # 找到字符在字母表中的位置，并进行移位
                index = (alphabet.find(char) - key) % 26
                plaintext += alphabet[index]
            else:
                # 非字母字符不变
                plaintext += char
        print(f"Key {key}: {plaintext}")


def decrypt_caesar_cipher_ascii(ciphertext):
    """对给定的密文进行凯撒密码的暴力破解，使用ASCII码进行偏移，尝试每一种可能的移位，并打印结果。"""
    # ASCII的可打印字符从空格(32)到波浪号(126)
    for key in range(95):  # 因为有95个可打印的ASCII字符
        plaintext = ''
        for char in ciphertext:
            if 32 <= ord(char) <= 126:
                # 计算偏移后的ASCII码，并进行转换
                new_char = chr(32 + ((ord(char) - 32) - key) % 95)
                plaintext += new_char
            else:
                # 对于非可打印的字符，直接添加到结果中
                plaintext += char
        print(f"Key {key}: {plaintext}")


def brute_force_caesar_cipher(encrypted_text):
    # 定义解密凯撒密码的内部函数
    def decrypt_caesar_cipher(text, shift_1):
        decrypted_text = ""

        for char in text:
            # 检查字符是否为字母
            if char.isalpha():
                # 根据偏移量计算新的字符位置
                shifted = ord(char) - shift_1

                # 如果字符超出字母范围，则进行回绕
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26

                decrypted_text += chr(shifted)
            else:
                # 对于非字母字符，不进行偏移
                decrypted_text += char
        return decrypted_text

    # 尝试所有可能的偏移量从1到25
    for shift in range(1, 26):
        # 对每个偏移量解密密文
        decrypted_message = decrypt_caesar_cipher(encrypted_text, shift)
        # 直接打印每个偏移量的解密结果
        print(f"shift {shift}: {decrypted_message}")


def decrypt_vigenere(ciphertext_1, key_1):
    # 将密钥转换为小写
    key_1 = key_1.lower()
    # 初始化解密后的文本
    decrypted_1 = ''
    # 初始化密钥索引
    key_index = 0
    # 遍历密文
    for char in ciphertext_1:
        # 如果字符是字母，则进行解密
        if char.isalpha():
            # 将密文和密钥字符转换为0-25的数字
            char_index = ord(char.lower()) - ord('a')
            key_char_index = ord(key_1[key_index % len(key_1)]) - ord('a')
            # 进行解密：将密文字符减去密钥字符的位置
            decrypted_char = chr((char_index - key_char_index) % 26 + ord('a'))
            # 将解密后的字符添加到结果中
            decrypted_1 += decrypted_char
            # 更新密钥索引
            key_index += 1
        # 如果字符不是字母，直接添加到结果中
        else:
            decrypted_1 += char
    return decrypted_1


def remove_non_letters(text):
    # 使用列表推导式和str.isalpha()检查每个字符是否是字母
    cleaned_text = ''.join([char for char in text if char.isalpha()])
    return cleaned_text


def boom_vigenere(ciphertext_1, know_1):
    maby_key = decrypt_vigenere(ciphertext_1, know_1)
    maby_key = remove_non_letters(maby_key)
    print('[INFO]' + maby_key)
    for i in range(2, len(maby_key) + 1):
        substring = maby_key[:i]
        if len(substring) > len(know_1):
            return
        print('key:' + substring + '-->' + decrypt_vigenere(ciphertext_1, substring))


def decrypt_affine_cipher(y_hex, m, known_plaintext):
    """ 使用穷举法破解仿射密码。

    参数:
    y_hex -- 十六进制表示的密文字符串
    m -- 模数（例如，全ASCII字符就是256）
    known_plaintext -- 已知的明文开头

    返回:
    (a, b, plaintext) -- 解密所用的a, b值和解密后的明文
    """

    def egcd(a_1, b_1):
        """ 扩展欧几里得算法 """
        if a_1 == 0:
            return b_1, 0, 1
        else:
            g, y_1, x = egcd(b_1 % a_1, a_1)
            return g, x - (b_1 // a_1) * y_1, y_1

    def modinv(a_1, m_1):
        """ 计算模逆元素 """
        g, x, _ = egcd(a_1, m_1)
        if g != 1:
            return None  # 模逆不存在
        else:
            return x % m_1

    # 将十六进制字符串转换为整数列表
    y = [int(y_hex[i:i + 2], 16) for i in range(0, len(y_hex), 2)]

    # 尝试每一个可能的a值（必须与m互质）
    for a in range(1, m):
        if egcd(a, m)[0] == 1:  # 确保a和m互质
            a_inv = modinv(a, m)
            if a_inv is None:
                continue
            for b in range(m):
                # 尝试解密
                decrypted_bytes = [(a_inv * (byte - b) % m) for byte in y]
                plaintext = ''.join(chr(byte) for byte in decrypted_bytes)
                # 检查已知明文是否匹配
                if plaintext.startswith(known_plaintext):
                    return a, b, plaintext
    return None  # 如果没有找到有效的解密结果

def decrypt_rail_fence(cipher_text, num_rails):
    # 创建一个列表来跟踪每条轨道的字符位置
    rail_pattern = [[] for _ in range(num_rails)]
    rail = 0
    direction = 1  # 控制轨道的变化方向

    # 模拟加密过程中字符的分布
    for i in range(len(cipher_text)):
        rail_pattern[rail].append(i)
        rail += direction

        # 当到达第一条或最后一条轨道时改变方向
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    # 按照轨道顺序重建消息
    result = [''] * len(cipher_text)
    idx = 0
    for rail_list in rail_pattern:
        for position in rail_list:
            result[position] = cipher_text[idx]
            idx += 1

    return ''.join(result)

def brute_force_rail_fence(cipher_text):
    # 尝试从2轨到密文长度的所有轨道数
    for num_rails in range(2, len(cipher_text) + 1):
        decrypted_text = decrypt_rail_fence(cipher_text, num_rails)
        print(f"[INFO]尝试 {num_rails} 轨道: {decrypted_text}")

def boom():
    while True:
        print('''
===========================
boom tools
1:caesar
凯撒爆破(基于字典)
2:caesar1
基于ascii
3:caesar2
不包含符号
4:Vigenère
已知开头部分明文例如‘flag’爆破所有可能
5:Affine Cipher(仿射密码)
y=(ax+b) mod m 
需要m,y_hex,known_plaintext
6:Fence boom
栅栏密码爆破
===========================
''')
        choice = int(input('-->'))
        if choice == 1:
            caesar_1(input('密文-->'), input('字典-->'))
        if choice == 2:
            decrypt_caesar_cipher_ascii(input('密文-->'))
        if choice == 3:
            brute_force_caesar_cipher(input('-->'))
        if choice == 4:
            boom_vigenere(input('密文-->'), input('已知-->'))
        if choice == 5:
            m = int(input('m-->'))
            y = input('y-->')
            known_plaintext = input('known_plaintext-->')
            try:
                a, b, plaintext = decrypt_affine_cipher(y, m, known_plaintext)
                print(f"解密成功！a={a}, b={b}, 明文: {plaintext}")
            except Exception as e:
                print(str(e))
        if choice == 6:
            brute_force_rail_fence(str(input('-->')))
        else:
            return 0