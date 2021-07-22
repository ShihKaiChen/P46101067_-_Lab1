class Nine_Coins:
    def __init__(self, decimal, binary=0, HT=0):
        self.decimal = decimal
        self.binary = binary
        num = []
        m = self.decimal
        for n in range(9):
            a = m // (2)
            b = m % (2)
            num += [str(b)]
            m = a
            self.binary = ''.join(num[::-1])
        for n in range(9):
            if num[n] == '0':
                num[n] = 'H'
            else:
                num[n] = 'T'
        self.HT = ''.join(num[::-1])

    def __str__(self):
        return f'binary: {self.binary} and decimal: {self.decimal}'

    def __repr__(self):
        return f'Nine_Coins:{self.HT}'

    def toss(self):
        from random import randint
        self.decimal = randint(0, 512)
        num = []
        m = self.decimal
        for n in range(9):
            a = m // (2)
            b = m % (2)
            num += [str(b)]
            m = a
            self.binary = ''.join(num[::-1])
        for n in range(9):
            if num[n] == "0":
                num[n] = 'H'
            else:
                num[n] = 'T'
        self.HT = ''.join(num[::-1])