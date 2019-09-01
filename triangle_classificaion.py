class Triangle:
    def __init__(self,s1,s2,s3):
        self.a = s1
        self.b = s2
        self.c = s3
    def triangle_right(self):

        return (self.a**2)+(self.b**2)== (self.c**2) or (self.a**2)+(self.c**2)==(self.b**2) or (self.b**2)+(self.c**2)==(self.a**2)


    def triangle_isosceles(self):
        return ((self.a ==self.b) or (self.a ==self.c) or (self.b ==self.c)) and ((self.a+self.b>self.c)and(self.a+self.c>self.b) and (self.b+self.c>self.a))


    def triangle_scalene(self):
        return (self.a!=self.b) and (self.b!=self.c) and (self.a!=self.c) and ((self.a+self.b>self.c) and (self.a+self.c>self.b) and (self.b+self.c>self.a))

    def triangle_equilateral(self):
        return (self.a==self.b) and (self.b ==self.c) and ((self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a))
