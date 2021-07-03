# (a+bi)(c+di) = (ac−bd) + (ad+bc)i

# class Complex:
#     def __init__(self, r, i):
#         self.real = r 
#         self.imaginary = i

#     def __add__(self, c):
#         return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
#     def __mul__(self, c):
#         mulReal =  self.real*c.real - self.imaginary*c.imaginary
#         mulImg =  self.real*c.imaginary + self.imaginary*c.real
#         return Complex(mulReal, mulImg)

#     def __str__(self):
#         if self.imaginary<0:
#             return f"{self.real} - {-self.imaginary}i"
#         else:
#             return f"{self.real} + {self.imaginary}i"

# c1 = Complex(1, -4)
# c2 = Complex(331, -37)  
# print(c1 + c2)
# print(c1 * c2)


class employe:
    def __init__(self,i,j):
        self.num=i
        self.num2=j
    def __add__(self,c):
        # print("hey buddy")
        return employe(self.num+c.num,self.num2+c.num2)
    def __mul__(self,c):
        realdf=self.num*c.num-self.num2*c.num2
        imgf=self.num*c.num2-self.num2*c.num
        return employe(realdf,imgf)
        
    def __str__(self):
        return f"{self.num}+{self.num2}i"
e1=employe(3,2)
e2=employe(1,7) 
print(e1+e2)
print(e1*e2)