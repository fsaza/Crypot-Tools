from Crypto.Cipher import AES


def crypto_cipher_aes(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    d = aes.decrypt(data)
    return d


def aes_1():
    while True:
        print('''
========================================
AES Tools
1:Crypto.Cipher
解密基于Crypto.Cipher的AES
========================================
''')
        choose = int(input('-> '))
        if choose == 1:

            data_bytes = input('密文-->')
            try:
                # 使用 ast.literal_eval 安全地评估字符串
                # 首先将输入字符串转换为它在 Python 字节字面值中的形式
                byte_string = "b'" + data_bytes.replace("'", "\\'") + "'"
                data_bytes = eval(byte_string)
            except Exception as e:
                print(f"转换错误：{e}")
            key_hex = input('Key--> ')
            iv_hex = input('IV--> ')

            decrypted_data = crypto_cipher_aes(key_hex, iv_hex, data_bytes)
            print("解密结果:", decrypted_data.decode('utf-8', errors='ignore'))
            break
        else:
            return
