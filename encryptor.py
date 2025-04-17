def encrypt(s):
    rev = s[::-1]
    po = len(rev) // 2 + 1
    fh = rev[:po]
    sh = rev[po:]
    res = sh + fh
    return res

#a = input()
#print(encrypt(a))