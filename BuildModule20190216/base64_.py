import base64

a = base64.b64encode(b'binary\x00string')
print(a)
b = base64.b64decode(a)
print(b)

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))




















