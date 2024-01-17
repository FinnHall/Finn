
class Polynomial:
    def __init__(self):
        self.polynomial = ''
        self.factored = ''

        self.GCF = ''
        self.Max = ''
        self.Min = ''

    def generate(self):
        self.GCF = 'x2'
        self.Max = '2'
        self.Min = ''


        self.polynomial = f'{self.GCF}({}{})({}{}) '


    def combine(self):
        pass

    def check(self):
        pass

#  x2 + 9x + 18
# (x + 6)(x + 3)
# [x, 6] * [x, 3]
# [x2, 3x, 6x, 18]

# x2(x - 6)(x2 + 10)
# x2(x3 + 10x - 6x2 - 60)
# x2(x3 - 6x2 + 10x - 60)
# x5 - 6x4 + 10x3 - 60x2
