def gcd(m,n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

def lcd(m,n):
    return m * n // gcd(m, n)

class Fraction:
    def __init__(self,top,bottom):
        if type(top) != int or type(bottom) != int:
            raise RuntimeError("Your fraction must use ints")
        self.common = gcd(top, bottom)
        self.num = top // self.common
        self.den = bottom // self.common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
     
    def __mul__(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        return Fraction(newnum, newden)
              
    def __div__(self, other):
        newnum = self.num*other.den
        newden = self.den*other.num
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num*other.den
        newden = self.den*other.num
        return Fraction(newnum, newden)
                  
    def __sub__(self, other):
        num1 = self.num*other.den
        num2 = other.num*self.den
        newnum = num1 - num2
        newden = other.den*self.den
        return Fraction(newnum, newden)
                    
    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum  
                    
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum
     
    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum != secondnum


if __name__ == "__main__":
    x = Fraction(3,4)
    y = Fraction(1,2)
    a = Fraction(1,-4)
    b = Fraction(-1,4)
    c = Fraction(-3,-4)

    assert x != y
    assert x > y
    assert (x-y) == Fraction(1, 4)
    assert (x+y) == Fraction(5, 4)
    assert x.getDen() == 4
    assert a == b
    assert x == c