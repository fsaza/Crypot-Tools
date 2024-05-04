import os
import subprocess
import threading
import time
from tools.rw import *
import re

def yafu(number):
    # 构建 yafu 程序的完整路径
    yafu_path = os.path.join(os.getcwd()[:-11], 'Required', 'yafu', "yafu-x64.exe")
    # 执行 yafu 程序,并捕获输出
    with subprocess.Popen([yafu_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          universal_newlines=True) as proc:
        # 向 yafu 程序写入数据
        proc.stdin.write('factor(' + number + ')')
        proc.stdin.flush()

    return 1

def yafu_get(number):
    delete_files(os.path.join(os.getcwd(), 'factor.log'))
    yafu1 = threading.Thread(target=yafu, args=(number,))
    yafu1.start()
    while True:
        data = read_file(os.path.join(os.getcwd(), 'factor.log'))
        time.sleep(1)
        print("Debug - data:", data)  # 调试输出，查看 data 的值
        if 'Total factoring time =' in str(data):
            # 使用正则表达式匹配因子和结束标记
            pattern = r'div: found prime factor = (\d+)'
            matches = re.findall(pattern, data)
            print("Debug - matches:", matches)  # 调试输出，查看匹配的结果

            factors = [int(match) for match in matches]

            if factors:  # 检查是否有匹配的因子
                # 找到最后一个因子的下一个数字的索引
                last_factor_index = data.rfind(matches[-1]) + len(matches[-1])
                end_index = data.find('Total factoring time', last_factor_index)

                # 提取最后一个因子的下一个数字
                last_number = int(data[last_factor_index:end_index].split()[-1])
                return factors, last_number
            else:
                pattern = r'prp10 = (\d+)'
                matches = re.findall(pattern, data)
                print("Debug - matches:", matches)  # 调试输出，查看匹配的结果

                factors = [int(match) for match in matches]

                if factors:  # 检查是否有匹配的因子
                    return factors
                else:
                    print("No factors found!")  # 调试输出，没有找到匹配的因子
                    return None

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def inverse_mod(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"{a} 没有模 {m} 的逆元素")
    else:
        return x % m

def n_c_e_to_m(n, c, e):
    factors = yafu_get(str(n) + '\n\n')  # 将参数转换为字符串类型

    # 计算 phi
    phi = 1
    for factor in factors:
        phi *= factor - 1

    # 计算 d
    d = inverse_mod(e, phi)

    # 解密消息
    m_hex = hex(pow(c, d, n))[2:]
    m_bytes = bytes.fromhex(m_hex)

    return m_bytes.decode('utf-8')

n = 17290066070594979571009663381214201320459569851358502368651245514213538229969915658064992558167323586895088933922835353804055772638980251328261
c = 14322038433761655404678393568158537849783589481463521075694802654611048898878605144663750410655734675423328256213114422929994037240752995363595
e = 65537
print(n_c_e_to_m(n, c, e))
