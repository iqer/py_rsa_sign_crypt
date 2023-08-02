"""
gzip压缩与解压缩数据流与文件流
"""
import binascii
import gzip
from io import BytesIO


def gzip_compress(raw_data: str) -> bytes:
    buf = BytesIO()
    f = gzip.GzipFile(mode='wb', fileobj=buf)
    bin_data = raw_data.encode('utf-8')
    try:
        f.write(bin_data)
    finally:
        f.close()
    return buf.getvalue()


def gzip_uncompress(c_data: bytes) -> str:
    buf = BytesIO(c_data)
    f = gzip.GzipFile(mode='rb', fileobj=buf)
    try:
        r_data = f.read()
    finally:
        f.close()
    return r_data.decode('utf-8')


def compress_file(fn_in, fn_out):
    f_in = open(fn_in, 'rb')
    f_out = gzip.open(fn_out, 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()


def uncompress_file(fn_in, fn_out):
    f_in = gzip.open(fn_in, 'rb')
    f_out = open(fn_out, 'wb')
    file_content = f_in.read()
    f_out.write(file_content)
    f_out.close()
    f_in.close()


if __name__ == '__main__':
    in_data = 'hello, world!'
    print(in_data)
    out_data = gzip_compress(in_data)
    print(binascii.hexlify(out_data))

    r_data = gzip_uncompress(out_data)
    print(r_data)
