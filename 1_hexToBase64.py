from binascii import unhexlify, b2a_base64, hexlify
string =input()

ans = b2a_base64(unhexlify(string))



print(ans)

print(type(ans))

if ans == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n': #\n?
    print('successful')

# string = raw_input()
# ans = string.decode('hex').encode('base64')

# print(ans)
