class Message(object):
    def __init__(self, text):
        self.message_text = text

    def get_message_text(self):
        return self.message_text

    def build_shift_dict(self, shift):
        sdict = {}
        i = ord('a')
        while i <= ord('z'):
            if i + shift <= ord('z'):
                sdict[chr(i)] = chr(i + shift)
            elif i + shift > ord('z'):
                sdict[chr(i)] = chr(i + shift - 26)
            i+=1
        i = ord('A')
        while i <= ord('Z'):
            if i + shift <= ord('Z'):
                sdict[chr(i)] = chr(i + shift)
            elif i + shift > ord('Z'):
                sdict[chr(i)] = chr(i + shift - 26)
            i+=1
        return sdict
    def apply_shift(self, shift):
        shifted = ''
        for k in self.message_text:
            if k.isalpha():
                if (k.islower() and ord(k)+shift > ord('z')) or (k.isupper() and ord(k)+shift > ord('Z')):
                    shifted += chr(ord(k) + shift - 26)
                else:
                    shifted += chr(ord(k) + shift)
            else:
                shifted += k
        return shifted

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        self.message_text = text
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        return self.shift

    def get_encryption_dict(self):
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

class CiphertextMessage:
    def __init__(self, text, shift):
        self.text = text
        self.shift = shift

    def build_reverse_shift_dict(self):
        sdict = {}
        i = ord('a')
        while i <= ord('z'):
            sdict[chr(i)] = chr(i - self.shift)
            i+=1
        i = ord('A')
        while i <= ord('Z'):
            sdict[chr(i)] = chr(i - self.shift)
            i+=1
        return sdict

    def decrypt_message(self):
        unshifted = ''
        for k in self.text:
            if k.isalpha():
                if (k.islower() and ord(k)+self.shift < ord('a')) or (k.isupper() and ord(k)+self.shift < ord('A')):
                    unshifted += chr(ord(k) - self.shift + 26)
                else:
                    unshifted += chr(ord(k) - self.shift)
            else:
                unshifted += k
        return unshifted

### Test cases
if __name__ == '__main__':
    # Test PlaintextMessage
    plaintext1 = PlaintextMessage('Hello, World!', 4)
    print('Expected: Lipps, Asvph!')
    print('Actual: ', plaintext1.get_message_text_encrypted())
    plaintext2 = PlaintextMessage('abcdef', 2)
    print('Expected: cdefgh')
    print('Actual: ', plaintext2.get_message_text_encrypted())
    # Example 1
    msg = CiphertextMessage('Khoor Zruog!', 3) # Encrypted with shift=3
    print('Expected: Hello World!')
    print('Actual :', msg.decrypt_message())
    # Example 2
    msg2 = CiphertextMessage('Wklv lv d whvw phvvdjh.', 3)
    print('Expected: This is a test message.')
    print('Actual :', msg2.decrypt_message())
    # Example 3
    msg3 = CiphertextMessage('Fdhvdu flskhu lv vlpsoh.', 3)
    print('Expected: Caesar cipher is simple.')
    print('Actual :', msg3.decrypt_message())