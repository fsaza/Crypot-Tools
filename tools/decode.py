def decode_10_to_16():
    print(hex(int(input('-->'))))


def decode_16_to_m():
    # 获取用户输入
    hex_input = input('-->')

    # 检查输入是否以 '0x' 开头，这是十六进制数的常见前缀
    if hex_input.startswith('0x'):
        hex_input = hex_input[2:]  # 去除 '0x' 前缀

    # 将十六进制字符串转换为基数为16的整数
    try:
        int(hex_input, 16)
    except ValueError:
        print("输入的不是有效的十六进制数字。")
        return

    # 将整数转换为字节数组，然后假设使用 UTF-8 编码解码为字符串
    try:
        decoded_string = bytes.fromhex(hex_input).decode('utf-8')
        print("[INFO]", decoded_string)
    except UnicodeDecodeError:
        # 使用错误处理策略 'replace'
        decoded_string = bytes.fromhex(hex_input).decode('utf-8', 'replace')
        print("[INFO] 解码后的字符串包含非 UTF-8 字符，已替换为占位符：", decoded_string)

def a_lower(text):
    print('[INFO]' + text.lower())


def a_upper(text):
    print('[INFO]' + text.upper())


def bytes_hex(text):
    try:
        a = eval(f'b"{text}"')  # 使用 f-string 插入文本
        print(a.hex())
    except SyntaxError as e:
        print("语法错误:", e)
    except Exception as e:
        print("发生错误:", e)

def hex_to_ten(hex_string):
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    try:
        # 使用内置的 int 函数将十六进制字符串转换为十进制整数
        decimal = int(hex_string, 16)
        return decimal
    except ValueError as e:
        print("输入错误:", e)
        return None

def long_to_bytes(n):
    # 计算需要的字节数，加上7是为了在除以8时可以向上取整
    byte_length = (n.bit_length() + 7) // 8
    return n.to_bytes(byte_length, 'big')
def decode_m():
    print('''
==================
decode tools
1:10   -> 16
2:16   -> m
3:A    -> a
4:a    -> A
5:bytes->hex
6:16   ->10
7:long ->bytes
==================
''')
    choice = int(input('-->'))
    if choice == 1:
        decode_10_to_16()
    if choice == 2:
        decode_16_to_m()
    if choice == 3:
        a_lower(input('-->'))
    if choice == 4:
        a_upper(input('-->'))
    if choice == 5:
        bytes_hex(input('-->'))
    if choice == 6:
        print(hex_to_ten(input('-->')))
    if choice == 7:
        print(long_to_bytes(input('-->')))
    else:
        return
