# X = [[1,2,3],  
#        [4,5,6],  
#        [7,8,9]]  
  
# Y = [[10,11,12],  
#        [13,14,15],  
#        [16,17,18]]  
  
# Result = [[0,0,0],  
#                 [0,0,0],  
#                 [0,0,0]]  
# # iterate through rows  
# for i in range(len(X)):  
#    # iterate through columns  
#    for j in range(len(X[0])):  
#         Result[i][j] = X[i][j] + Y[i][j]  
# for r in Result:  
#    print(r)  
def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            imp=int(input(f"Enter 0[{i}][{j}]"))
            row.append(imp)
        o.append(row)
    return o
def sum(A,B):
    output=[]
    for i in range(len(A)):    
        row=[]
        for j in range(len(A[0])):    
            row.append(A[i][j]+B[i][j])
        output.append(row)
    return output
m=int(input("Enter your value m:\n"))
n=int(input("Entert your next value n\n"))
print("enter your matrixA")
A=matrix(m,n)
print(A)

print("enter your matrixB")
B=matrix(m,n)
print(B)

s=sum(A,B)
print(s)













