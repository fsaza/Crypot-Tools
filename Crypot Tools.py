from tools.RSA import *
from tools.operation import *
from tools.boom import *
from tools.decode import *
from tools.AES import *
from tools.feature import *
print('''
==========================================================
\033[31mCrypto \033[33mtools
\033[34mby FSAZ\033[38m
注意,本软件存目前在任意命令执行,如果被恶意软件利用会导致提权！！！
==========================================================                        
''')


# 菜单
def main():
    while True:
        print('''
==================================
子集菜单输入任意不存在选项返回上级
1:operation
2:RSA tools
3:AES tools
4:boom tools
5:decode tools
6:find feature
==================================
''')
        choice = int(input('-->'))
        if choice == 1:
            operation_m()
        if choice == 2:
            rsam()
        if choice == 3:
            aes_1()
        if choice == 4:
            boom()
        if choice == 5:
            decode_m()
        if choice == 6:
            feature()
        else:
            print('[ERROR]')


main()
