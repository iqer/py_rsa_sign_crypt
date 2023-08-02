"""
生成CRC8签名信息
"""
import binascii

from crcmod import predefined


class CRCGenerator(object):
    def __init__(self):
        self.module = 'crc-8'

    def create(self, input_data: str) -> str:
        crc8 = predefined.Crc(self.module)
        hex_data = input_data
        print(hex_data)
        hex_data = binascii.unhexlify(hex_data)
        crc8.update(hex_data)
        result = hex(crc8.crcValue)
        print(result)
        return result


if __name__ == "__main__":
    crc = CRCGenerator()
    crc.create('1E00100463FA0F0219216800220260180524000110001611329355AA')
