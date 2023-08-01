import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
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


def rsa_private_sign(data: str) -> str:
    """
    私钥签名
    """
    private_key = get_key('rsa_private_key.pem')
    signer = PKCS1_signature.new(private_key)
    digest = SHA.new()
    digest.update(data.encode('utf-8'))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    signature = signature.decode("utf-8")
    return signature


def rsa_public_check_sign(text: str, sign: str) -> bool:
    """
    公钥验证签名
    """
    public_key = get_key('rsa_public_key.pem')
    verifier = PKCS1_signature.new(public_key)
    digest = SHA.new()
    digest.update(text.encode('utf-8'))
    return verifier.verify(digest, base64.b64decode(sign))


def _test_sign():
    msg = 'this is test sign text'
    sign = rsa_private_sign(msg)
    print(rsa_public_check_sign(msg, sign))


if __name__ == '__main__':
    _test_sign()
