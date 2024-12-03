class TComplex: 
    sep: str = '_'
   
    def __init__(self, re: float=None, im: float=None):
        if re is None and im is None:
            self.re = 1
            self.im = 0
        elif im is None:
            self.re = re
            self.im = 1
        else:
            self.re = re
            self.im = im
        
    def __str__(self):
        if self.im >= 0:
            return f"{self.re} + {self.im}i"
        else:
            return f"{self.re} - {-self.im}i"
            
    def __add__(self, addend):
        real = self.re + addend.re
        imag = self.im + addend.im
        return TComplex(real, imag)
    
    def __sub__(self, subtract):
        real = self.re - subtract.re
        imag = self.im - subtract.im
        return TComplex(real, imag)
    
    def __mul__(self, multiplier):
        if isinstance(multiplier, int):
            real = self.re * multiplier
            imag = self.im * multiplier
            return TComplex(real, imag)
        elif isinstance(multiplier, TComplex):
            real = self.re * multiplier.re - self.im * multiplier.im
            imag = self.re * multiplier.im + multiplier.re * self.im
            return TComplex(real, imag)

    def __truediv__(self, divider):
        if isinstance(divider, int):
            if divider == 0:
                raise ValueError("Division by zero")
            real = self.re / divider
            imag = self.im / divider
            return TComplex(real, imag)
        elif isinstance(divider, TComplex):
            denominator = divider.re**2 + divider.im**2
            if denominator == 0:
                raise ValueError("Division by zero")
            real = (self.re * divider.re + self.im * divider.im) / denominator
            imag = (self.im * divider.re - self.re * divider.im) / denominator
            return TComplex(real, imag)

    def __ne__(self, other):
        if isinstance(other, int):
            return self.re != other or self.im != 0
        elif isinstance(other, TComplex):
            return self.re != other.re or self.im != other.im
