import struct
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
a = struct.pack('>I', 10240099)
print(a)
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
b = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(b)

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00' \
    b'\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

c = struct.unpack('<ccIIIIIIHH', s)
print(c)














