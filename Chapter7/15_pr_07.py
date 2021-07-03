# n = 3
# for i in range(3): 
#     print(" " * (n-i-1), end="")
#     print("*" * (2*i+1), end="")
#     print(" " * (n-i-1))

# second Way >>>>>............
# a = int(input("eneter your no."))
# for i in range(a):
#     print(" "*(a-i-1),"* "*i)

# a = int(input("eneter your no."))
# for i in range(a):
#     print("* "*i," "*(a-i-1))

# a = int(input("eneter your no."))
# for i in range(a):
#     # for j in range(a):
#     print(" "*i,"*"*(a-i))


a = int(input("eneter your no."))
for i in range(a):
    # for j in range(a):
    print(" "*(i),"* "*(a-i))
 