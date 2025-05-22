class BasePolynomial:
    def __init__(self, coeffs):
        self.coeffs = list(coeffs) #coeffs[:]
        self._trim()

    def _trim(self):
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            del self.coeffs[-1]

    def __add__(self, other):
        i, j = len(self.coeffs),len(other.coeffs)
        result = []
        for k in range(min(i,j)):
            result.append(self.coeffs[k]+other.coeffs[k])
        if i>j:
            result.extend(self.coeffs[j:])
        else:
            result.extend(other.coeffs[i:])
        return self.__class__(result)
    def __sub__(self, other):
        i, j = len(self.coeffs),len(other.coeffs)
        result = []
        for k in range(min(i,j)):
            result.append(self.coeffs[k]-other.coeffs[k])
        if i>j:
            result.extend(self.coeffs[j:])
        else:
            result.extend(-other.coeffs[i:])
        return self.__class__(result)
    def __mul__(self, other):
        result = [0]*(len(self.coeffs)+len(other.coeffs)-1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i+j] += self.coeffs[i] * other.coeffs[j]
        return self.__class__(result)
    def __call__(self, x):
        result = 0
        for i in range(len(self.coeffs)):
            result += self.coeffs[i] * (x ** i)
        return result
    def __eq__(self, other):
        result = True
        if len(self.coeffs) == len(other.coeffs):
            for i in range(len(self.coeffs)):
                if self.coeffs[i] != other.coeffs[i]:
                    result = False
                else:
                    continue
        else:
            result = False
        return result
    def __str__(self):
        terms = []
        i = 0
        for c in list(self.coeffs):
            if c == 0:
                i += 1
                continue
            if i == 0:
                terms.append(f"{c}")
            elif i == 1:
                terms.append(f"{c}x")
            else:
                terms.append(f"{c}x^{i}")
            i += 1
        return " + ".join(terms) if terms else "0"
class CalculusPolynomial(BasePolynomial):
    def differentiate(self, n=1):
        tco = list(self.coeffs)
        for i in range(n):
            nco = [0] * (len(tco)-1)
            for j in range(1,len(tco)):
                nco[j-1] = tco[j] * j
            tco = nco
        return self.__class__(tco)
    def integrate(self):
        nco = [0] * (len(self.coeffs)+1)
        for i in range(len(self.coeffs)):
            nco[i+1]=self.coeffs[i] / (i+1)
        return self.__class__(nco)
# --------- MAIN for Polynomial Test ---------
print("=== Polynomial Calculator ===")
coeffs1 = list(map(int, input("Enter coeffs for poly1 (space-separated): ").split()))
coeffs2 = list(map(int, input("Enter coeffs for poly2 (space-separated): ").split()))
p1 = CalculusPolynomial(coeffs1)
p2 = CalculusPolynomial(coeffs2)
while True:
    cmd = input("\n1: Add\n2: Subtract\n3: Multiply\n4: Evaluate\n5: Differentiate\n6: Integrate\n7: Exit\n> ")
    if cmd == '1':
        print("p1 + p2 =", p1 + p2)
    elif cmd == '2':
        print("p1 - p2 =", p1 - p2)
    elif cmd == '3':
        print("p1 * p2 =", p1 * p2)
    elif cmd == '4':
        x = float(input("x = "))
        print("p1(x) =", p1(x))
    elif cmd == '5':
        n = int(input("Order of derivative: "))
        print("d^{}(p1)/dx^{} =".format(n, n), p1.differentiate(n))
    elif cmd == '6':
        print("Integral of p1 =", p1.integrate())
    elif cmd == '7':
        break