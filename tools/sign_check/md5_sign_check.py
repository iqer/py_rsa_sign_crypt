"""
生成MD5摘要信息
"""
import hashlib


def md5_digest(input_data: str) -> str:
    m = hashlib.md5()
    m.update(str.encode(input_data))
    print(m.hexdigest())
    return m.hexdigest()


if __name__ == '__main__':
    data = 'demo'
    md5_digest(data)
