from  binascii import unhexlify, b2a_base64

# # string = input()
# # string = unhexlify(string)
# # cip = unhexlify('686974207468652062756c6c277320657965')

# a_list = [chr(ord(a) ^ ord(b)) for a,b in zip(s1, s2)]
# ans = ''.join(a_list) 


# # ans = string ^ xor

# print()

def xor(s1,s2):
    return bytes([x^y for x,y in zip(s1,s2)])

s1 = unhexlify('1c0111001f010100061a024b53535009181c')
s2 = unhexlify('686974207468652062756c6c277320657965')
ans = unhexlify('746865206b696420646f6e277420706c6179')
print(s1,s2,ans)
if (xor(s1,s2) == ans):
    print('yay')
    print(xor(s1,s2))

