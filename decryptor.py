def decrypt(s):
    po = len(s)//2
    sh = s[:po]
    fh = s[po:]
    rev = fh + sh
    res = rev[::-1]
    return res

#a = input()
#print(decrypt(a))