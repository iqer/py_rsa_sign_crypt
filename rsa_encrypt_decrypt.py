"""
RSA加解密
"""
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


def get_key(key_file: str) -> object:
    """获取key字符串值

    Args:
        key_file: 密钥路径字符串

    Returns:
        key密钥对象
    """
    with open(key_file) as f:
        data = f.read()
        key = RSA.importKey(data)
    return key


def encrypt_data(msg: str) -> str:
    """公钥加密数据

    Args:
        msg: 待加密字符串数据

    Returns:
        公钥加密的字符串数据
    """
    public_key = get_key('rsa_public_key.pem')
    cipher = PKCS1_cipher.new(public_key)
    encrypt_text = base64.b64encode(cipher.encrypt(bytes(msg.encode("utf8"))))
    return encrypt_text.decode('utf-8')


def decrypt_data(encrypt_msg: str) -> str:
    """私钥解密数据

    Args:
        encrypt_msg: 公钥加密后的字符串数据

    Returns:
        解密后的字符串数据
    """
    private_key = get_key('rsa_private_key.pem')
    cipher = PKCS1_cipher.new(private_key)
    back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)
    return back_text.decode('utf-8')


def _test_encrypt_decrypt():
    msg = "this is demo text crypt and decrypt"
    encrypt_text = encrypt_data(msg)
    decrypt_text = decrypt_data(encrypt_text)
    print(msg == decrypt_text)


if __name__ == '__main__':
    _test_encrypt_decrypt()
