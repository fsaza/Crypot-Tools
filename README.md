# Crypot-Tools
密码学解码工具
目前还不完善，欢迎所有人改进代码
目前实现

#根据正则表达式扫描特征
#AES Tools
1:Crypto.Cipher
解密基于Crypto.Cipher的AES

#boom tools
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

#decode tools
1:10   -> 16
2:16   -> m
3:A    -> a
4:a    -> A
5:bytes->hex
6:16   ->10
7:long ->bytes

#operation
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

#RSA TOOLS
1:p q e -> d
2:p q e c -> m
3:p q dp dq c-> m
4:e n dp c -> m
5:small d
  e n -> d
6:c d n -> m
7:n=small * x
m c e -> m

#参与贡献的作者
#FSAZ
