class Locker:
    def __init__(self, password):
        self.__password = password
        self.__data = ''
        self.__state = 'LOCKED'
        self.__fails = 0
    def unlock(self, password):
        if self.__state == 'LOCKED_OUT':
            print('Locker permanently locked out after 3 failed attempts.')
        elif self.__state == 'UNLOCKED':
            print('Locker is already unlocked.')
        elif password == self.__password:
            self.__state = 'UNLOCKED'
            print('Unlocked successfully,')
        elif password != self.__password:
            print('Incorrect password.')
            self.__fails +=1
            if self.__fails >= 3:
                print('Locker permanently locked out after 3 failed attempts.')
                self.__state ='LOCKED_OUT'
    def lock(self):
        if self.__state == 'UNLOCKED':
            self.__state = 'LOCKED'
        else:
            print('Locker is already locked.')
    def set_data(self, data):
        if self.__state == 'LOCKED' or self.__state == 'LOCKED_OUT':
            print('The locker is not unlocked.')
        elif self.__state == 'UNLOCKED':
            self.__data = data
    def get_data(self):
        if self.__state == 'LOCKED' or self.__state == 'LOCKED_OUT':
            print('The locker is not unlocked.')
        elif self.__state == 'UNLOCKED':
            print(self.__data)
# --------- MAIN for Simplified Locker Test ---------
print("=== Simplified Locker System ===")
pw = input("Set password for locker: ")
locker = Locker(pw)
while True:
    cmd = input("\n1: Unlock\n2: Lock\n3: Set data\n4: Get data\n5: Exit\n> ")
    if cmd == '1':
        pw_try = input("Enter password: ")
        locker.unlock(pw_try)
    elif cmd == '2':
        locker.lock()
    elif cmd == '3':
        data = input("Enter data to store: ")
        locker.set_data(data)
    elif cmd == '4':
        locker.get_data()
    elif cmd == '5':
        break