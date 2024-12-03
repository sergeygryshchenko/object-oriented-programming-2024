class TRational: 
    sep: str = '/'

    def __init__(self, num: int=None, denom: int=None):
        if num is None and denom is None:
            self.num = 1
            self.denom = 1
        elif denom is None:
            self.num = num
            self.denom = 1
        else:
            if denom != 0:
                self.num = num
                self.denom = denom
            else:
                raise TypeError("Invalid denominator")

       
    def __str__(self):
        if self.num == 0:
            return f'0'
        else:
            return f'{self.num}/{self.denom}'
            
    def __add__(self, addend):
        if isinstance(addend, TRational):
            num = self.num * addend.denom + addend.num * self.denom
            denom = self.denom * addend.denom
            return TRational(num, denom)
        elif isinstance(addend, int):
            num = self.num + addend * self.denom
            return TRational(num, self.denom)
    
    def __sub__(self, subtract):
        if isinstance(subtract, TRational):
            num = self.num * subtract.denom - subtract.num * self.denom
            denom = self.denom * subtract.denom
            return TRational(num, denom)
        elif isinstance(subtract, int):
            num = self.num - subtract * self.denom
            return TRational(num, self.denom)
    
    def __mul__(self, multiplier):
        if isinstance(multiplier, TRational):
            num = self.num * multiplier.num
            denom = self.denom * multiplier.denom
            return TRational(num, denom)
        elif isinstance(multiplier, int):
            num = self.num * multiplier 
            return TRational(num, self.denom)
        
    def __truediv__(self, divider):
        if isinstance(divider, TRational):
            num = self.num * divider.denom
            denom = self.denom * divider.num
            return TRational(num, denom)
        elif isinstance(divider, int):
            denom = self.denom * divider 
            return TRational(self.num, denom)

    def __ne__(self, other):
        return (self.num/self.denom) != other 
