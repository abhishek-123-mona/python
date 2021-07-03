# def maximum(num1,num2,num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3    
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

# m=maximum(300,598,80)
# print("The value of maximum is"+str(m))
















# n=int(input("Enter the three value"))
# i=1
# while i<n: 
    
def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    if(num2>num1):
        if(num2>num3):
                return num2
        else:
            return num3
m=maximum(50,60,80)
print("the value is"+str(m))
# i=i+1
