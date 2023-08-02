"""
DES加解密
密钥填充格式: ECB，填充方式: zeropadding
"""
import binascii

from pyDes import des, PAD_PKCS5


def des_encrypt_data(secret_key: str, s: str) -> bytes:
    iv = secret_key
    k = des(key=secret_key, IV=iv)
    en = k.encrypt(data=s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_decrypt_data(secret_key: str, s: bytes) -> str:
    iv = secret_key
    k = des(secret_key, IV=iv, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode('utf-8')


def _test_encrypt_decrypt():
    input_data = 'this is original text text.'
    secret_str = des_encrypt_data('12345678', input_data)
    output_data = des_decrypt_data('12345678', secret_str)
    assert output_data == input_data, '加解密数据不一致'


if __name__ == '__main__':
    _test_encrypt_decrypt()
