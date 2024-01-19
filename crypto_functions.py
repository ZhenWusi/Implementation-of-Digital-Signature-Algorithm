from numpy import gcd
import sympy
def generate_prime(bits=512):
    """生成一个指定位数的素数,默认512比特"""
    return sympy.randprime(2**(bits-1), 2**bits)
def generatePublicKey():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p-1)*(q-1)
    e = generate_prime(16)
    while sympy.gcd(e, phi_n) != 1:
        e = generate_prime(16)
    return e, n, phi_n
def generatePrivateKey(a, p, b=1):
    """
    生成 RSA 中的私钥的函数。
    使用替换变量的比较求解。
    将 b 更改为 b + p * k。
    """
    k = 1
    r = gcd(a, p)
    if r != 1:
        p = p // r
    while True:
        if (b + p * k) % a == 0:
            return (b + p * k) // a
        k += 1
def sign(hash, privKey, secondPartPubKey):
    """
    此函数返回签名，其计算使用文本或文件的现有哈希，公钥的第一部分和公钥的第二部分。
    参数以十六进制视图给出。我们必须将它们格式化为十进制视图，以成功计算哈希。
    :参数 hash - 文本或文件的哈希
    """
    hashInt = int(hash, 16)
    privKey = int(privKey, 16)
    secondPartPubKey = int(secondPartPubKey, 16)
    # 从十六进制转换为十进制，以便进行后续的计算
    signature = pow(hashInt, privKey, secondPartPubKey)
    # 使用模幂运算（pow 函数）计算哈希的私钥次方，对 secondPartPubKey 取模
    return signature
def check(signature, firstPartPubKey, secondPartPubKey):
    """
    此函数返回使用现有签名，公钥的第一部分e和公钥的第二部分d计算的哈希。
    参数以十六进制视图给出。我们必须将它们格式化为十进制视图，以成功计算哈希。
    """
    signature = int(signature, 16)
    firstPartPubKey = int(firstPartPubKey, 16)
    secondPartPubKey = int(secondPartPubKey, 16)
    hash = pow(signature, firstPartPubKey, secondPartPubKey)
    return hash
